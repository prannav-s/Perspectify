from django.shortcuts import render, redirect
# Create your views here.
from .forms import TextInputForm
from .models import TextInput
from .functions import WebScrape, generate_prompt
import openai
import re
import os

# Load environment variables from .env file

env_file_path = "app/.env"

# Read the API key from the .env file
openai.api_key = None
with open(env_file_path, "r") as env_file:
    for line in env_file:
        if line.startswith("OPENAI_API_KEY="):
            openai.api_key = line.strip().split("=")[1]
            break

# openai.api_key_path = '/Users/robelmelaku/Desktop/Perspectify/app/.env'

def extract_links_from_text(text):
    # Using regular expression to find URLs in the text
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return urls

def remove_alternative_sources_and_after(text):
    # Remove all text after the sentence starting with "Alternative news sources: "
    modified_text = text.split("Alternative news sources: ")[0]
    return modified_text

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
    instance = TextInput.objects.get(id=instance_id)
    
    # Perform our features on instance.url here
    

    # First we need to call the function that will scrape the link
    # text = scrape_function(instance.url)
    myscraper = WebScrape()
    web_page = myscraper.fetch_url(instance.url)
    text = myscraper.parse_html_content(web_page)
    
    
    # Second we need to call the summary function to summarize the text
    # summary = summary_function(text)
    
    # Third we need to call the primary and secondary viewpoints functions
    # primary = primary_function(text)
    # secondary = secondary_function(text)
    
    # Lastly, the resources function which will render the additional sources for the new viewpoints
    # resources = resources(viewpoints)
    
    # All these functions will be imported from the 'app/functions' file
    
    
    # The following lines will be later calling each function for each feature.
    # These are just demos to show on the website
    summary = 'Initial summary'
    primary = text
    secondary = text
    resources = text.split('.')[:5] # Later will be links to actual sites.
     
    
    # if request.method == 'POST':
    #     instance.text = request.POST.get('edited_url')
    #     instance.save()
    #     return redirect('analysis', instance_id=instance_id)
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(text),
        temperature=0.0,
        max_tokens=500,  # Adjust this value as needed

    )
    summary = "".join([i.text for i in response.choices ]) if response.choices else "No summary generated." 


    summary_links = extract_links_from_text(summary)
    
    resources = summary_links[2:]
    summary = remove_alternative_sources_and_after(summary)

    # primaryscraper = WebScrape()
    # primarypage = primaryscraper.fetch_url(summary_links[2])
    # primary = primaryscraper.parse_html_content(primarypage)
    # secondaryscraper = WebScrape()
    # secondarypage = secondaryscraper.fetch_url(summary_links[3])
    # secondary = secondaryscraper.parse_html_content(secondarypage)
    primary = summary_links[0]
    secondary = summary_links[1]
    return render(request, 'analysis.html', {'instance': instance, 'summary': summary, 'primary': primary, 'secondary': secondary, 'resources': resources})
