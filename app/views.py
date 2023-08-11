from django.shortcuts import render, redirect
# Create your views here.
from .forms import TextInputForm
from .models import TextInput
from .functions import *
import openai
import os
from dotenv import load_dotenv

# Read the API key from the .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


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
    

    # Call the function that will scrape the link
    myscraper = WebScrape()
    web_page = myscraper.fetch_url(instance.url)
    text = myscraper.parse_html_content(web_page)


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(text),
        temperature=0.0,
        max_tokens=500,  # Adjust this value as needed

    )
    
    # Call function to generate summary from the scraped text
    summary = "".join([i.text for i in response.choices ]) if response.choices else "No summary generated." 
    summary = remove_alternative_sources_and_after(summary)

    # Generate additional resources for requested source
    summary_links = extract_links_from_text(summary)
    resources = summary_links[2:]
    
    # Generate primary and secondary viewpoints for requested analysis
    primary = summary_links[0]
    secondary = summary_links[1]
    
    # Render each element using the written templates
    return render(request, 'analysis.html', {'instance': instance, 'summary': summary, 'primary': primary, 'secondary': secondary, 'resources': resources})