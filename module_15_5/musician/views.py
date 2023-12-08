from django.shortcuts import render,redirect
from . import forms
from . import models

from . import forms
# Create your views here.
def musician(request):
    if request.method == 'POST':
        Musician_form=forms.MusicianForm(request.POST)
        if Musician_form.is_valid():
            Musician_form.save()
            return redirect('album')
        else:
            print(Musician_form.errors)  
    else:
        Musician_form=forms.MusicianForm()
    
    return render(request,'musician.html',{'form':Musician_form})

def edit_musician(request, id):
    
    music_instance = models.Musician.objects.get(pk=id)

    if request.method == 'POST':
        
        Musician_form = forms.MusicianForm(request.POST, instance=music_instance)
        if Musician_form.is_valid():
            Musician_form.save()
            return redirect('homepage')
    else:
        
        Musician_form = forms.MusicianForm(instance=music_instance)

    return render(request, 'musician.html', {'form': Musician_form})