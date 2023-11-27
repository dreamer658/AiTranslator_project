from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoForm

def home(request):
    return HttpResponse("Welcome to the AITranslator")

def upload_video(request): #break it for me line by line
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES) #ask for what that line actually makes to understand post what the need of forms.py and the class meta
        if form.is_valid():
            form.save()
            #redirect to a new URL:
            return HttpResponse('/success/')
    else:
        form = VideoForm()
        
    return render(request, 'upload_video.html', {'form': form})