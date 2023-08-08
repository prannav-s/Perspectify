from django.shortcuts import render, redirect
# Create your views here.
from .forms import TextInputForm
from .models import TextInput
from .functions import summary

def index(request):
    return render(request, 'index.html')

def input_form(request):
    form = TextInputForm()
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('analysis', instance_id=instance.id)
    else:
        form = TextInputForm()
    return render(request, 'input_form.html', {'form': form})

def analysis(request, instance_id):
    instance = TextInput.objects.get(id=instance_id)
    
    # Perform our features on instance.url here
    

    # First we need to call the function that will scrape the link
    # text = scrape_function(instance.url)
    
    # Second we need to call the summary function to summarize the text
    # summary = summary_function(text)
    
    # Third we need to call the primary and secondary viewpoints functions
    # primary = primary_function(text)
    # secondary = secondary_function(text)
    
    # Lastly, the resources function which will render the additional sources for the new viewpoints
    # resources = resources(viewpoints)
    
    # All these functions will be imported from the 'app/functions' file
    
    
    summary = 'Summary here'
    primary = 'Primary viewpoint here' 
    secondary = 'Secondary viewpoint here'
    resources = 'Resources here'
    
    
    if request.method == 'POST':
        instance.text = request.POST.get('edited_url')
        instance.save()
        return redirect('analysis', instance_id=instance_id)
    return render(request, 'analysis.html', {'instance': instance, 'summary': summary, 'primary': primary, 'secondary': secondary, 'resources': resources})
