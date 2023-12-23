from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views import View


def musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('album')
        else:
            print(musician_form.errors)
    else:
        musician_form = forms.MusicianForm()

    return render(request, 'musician.html', {'form': musician_form})

class MusicianView(View):
    def post(self,request,*args,**kwargs):
        musician_form=forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('album')
    
    def get(self,request,*args,**kwargs):
        musician_form=forms.MusicianForm()
        return render(request, 'musician.html', {'form': musician_form})
    



def edit_musician(request, id):
    music_instance = models.Musician.objects.get(pk=id)

    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=music_instance)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    else:
        musician_form = forms.MusicianForm(instance=music_instance)

    return render(request, 'musician.html', {'form': musician_form})

def signup(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('signup')
    else:
        register_form = forms.RegistrationForm()
    
    return render(request, 'signup.html', {'form': register_form, 'type': 'Signup'})

class UserLoginView(LoginView):
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('homepage')
