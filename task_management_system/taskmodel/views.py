from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskModelForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else: 
        task_form=forms.TaskModelForm()

    return render(request,'add_task.html',{'form':task_form})



def edit_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task_form=forms.TaskModelForm(instance=task)

    if request.method == 'POST':
        task_form = forms.TaskModelForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')

    return render(request,'add_task.html',{'form':task_form})


def delete_task(request,id):
    task=models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task')