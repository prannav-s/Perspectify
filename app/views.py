from django.shortcuts import render, redirect
from .forms import TextInputForm
from .models import TextInput
from .functions import WebScrape, generate_prompt
import openai
import re
import os

try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

env_file_path = "app/.env"

# Read the API key from the .env file
openai.api_key = None
with open(env_file_path, "r") as env_file:
    for line in env_file:
        if line.startswith("OPENAI_API_KEY="):
            openai.api_key = line.strip().split("=")[1]
            break

def generate_summary(text):     
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize the following content:\n{text}",
        temperature=0.0,
        max_tokens=500  # Adjust the number of tokens as needed
        )
    return response.choices[0].text.strip()

def unique_link(link, domains):
    pattern = r'www\.([^.]+)\.com'
    domain = re.findall(pattern, link)
    if domains.__contains__(domain):
        return False
    domains.append(domain)
    return True

def create_links(term, domains):
    query = term
    search_query = f"{query} filetype:html"
    i = 0
    links = []
    for j in search(search_query, tld="com", num=10, stop=10, pause=0.1):
        if unique_link(j, domains):
            links.append(j)
            i += 1
            if i >= 10:
                break
    return links

def create_viewpoint(links, i):
    scraper = WebScrape()
    page = scraper.fetch_url(links[i])
    viewpoint = scraper.parse_html_content(page)
    return generate_summary(viewpoint) + " Link: " + links[i]

def find_search_term(text):
    search = text.split("Search: ")
    return search

def index(request):
    return render(request, 'index.html')

def input_form(request):
    form = TextInputForm()
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('analysis', instance_id=instance.id)
    return render(request, 'input_form.html', {'form': form})

def analysis(request, instance_id):
    domains = []
    instance = TextInput.objects.get(id=instance_id)
    myscraper = WebScrape()
    web_page = myscraper.fetch_url(instance.url)
    unique_link(instance.url, domains)
    text = myscraper.parse_html_content(web_page)

    response = openai.Completion.create(
        model="davinci-002",
        prompt=generate_prompt(text),
        temperature=0.0,
        max_tokens=500,  # Adjust this value as needed

    )
    summary = response.choices[0].text if response.choices else "No summary generated."
    term = find_search_term(summary)[1]
    summary = find_search_term(summary)[0]
    summary_links = create_links(term, domains)
    resources = summary_links
    primary = create_viewpoint(summary_links, 0)
    secondary = create_viewpoint(summary_links, 1)

    return render(request, 'analysis.html', {'instance': instance, 'summary': summary, 'primary': primary, 'secondary': secondary, 'resources': resources})
