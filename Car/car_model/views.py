from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from . import forms
from . import models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView
from .forms import CommentForm
from .models import Car,BuyCar
from django. contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Car
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DetailsPost(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

        
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    
def buy_car(request, id):
    post = get_object_or_404(Car, id=id)
    if post.quantity > 0:
        post.quantity -= 1
        post.save()
        BuyCar.objects.create(user=request.user, car=post)
        messages.success(request, 'Car purchased successfully!')
    else:
        messages.warning(request, 'All cars are sold out. Please look forward to new stock.')

    return redirect('detail_post',id)