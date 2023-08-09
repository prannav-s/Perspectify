from django.shortcuts import render, redirect
# Create your views here.
from .forms import TextInputForm
from .models import TextInput
from .functions import WebScrape, generate_prompt
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
# openai.api_key_path = '/Users/robelmelaku/Desktop/Perspectify/app/.env'

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
    primary = text.upper() 
    secondary = text.capitalize()
    resources = text.split('.')[:5] # Later will be links to actual sites.
     
    
    # if request.method == 'POST':
    #     instance.text = request.POST.get('edited_url')
    #     instance.save()
    #     return redirect('analysis', instance_id=instance_id)
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(text),
        temperature=0.6,
    )
    summary = response.choices[0].text if response.choices else "No summary generated."

    
    return render(request, 'analysis.html', {'instance': instance, 'summary': summary, 'primary': primary, 'secondary': secondary, 'resources': resources})
