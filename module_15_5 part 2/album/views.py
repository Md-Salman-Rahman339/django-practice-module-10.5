from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required,name='dispatch')
class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('album')

    def form_valid(self, form):
        form.instance.album = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        album_id = self.kwargs.get('id')
        if album_id:
            kwargs['instance'] = models.Album.objects.get(models.Album, id=album_id, album=self.request.user)
        return kwargs

@method_decorator(login_required,name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        id = self.kwargs.get("id")
        return get_object_or_404(models.Album, id=id)

@method_decorator(login_required,name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.get_object()
        return context
