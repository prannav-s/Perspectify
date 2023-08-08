from django.shortcuts import render, redirect
# Create your views here.
from .forms import TextInputForm
from .models import TextInput

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
    
    # Perform your analysis on instance.url here
    # This is where our function would take the link (instance.url) and render our desired outputs
    summary = instance.url
    primary = 'Primary viewpoint here' 
    secondary = 'Secondary viewpoint here'
    resources = 'Resources here'
    
    
    if request.method == 'POST':
        instance.text = request.POST.get('edited_url')
        instance.save()
        return redirect('analysis', instance_id=instance_id)
    return render(request, 'analysis.html', {'instance': instance, 'summary': summary, 'primary': primary, 'secondary': secondary, 'resources': resources})
