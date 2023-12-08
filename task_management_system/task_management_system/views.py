from django.shortcuts import render

from taskmodel.models import TaskModel


def show_task(request):
    data = TaskModel.objects.all()
    print(data)
    
    return render(request, 'show_task.html', {'data': data})
