from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
        else:
            print(album_form.errors)  
    else:
        album_form = forms.AlbumForm()
        
    return render(request, 'album.html', {'form': album_form})


def edit_album(request, id):
    
    album_instance = models.Album.objects.get(pk=id)

    if request.method == 'POST':
        
        album_form = forms.AlbumForm(request.POST, instance=album_instance)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    else:
        
        album_form = forms.AlbumForm(instance=album_instance)

    return render(request, 'album.html', {'form': album_form})