from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta: 
        model = TaskModel
        fields = '__all__'
        widgets = {
        'task_assign_date': forms.DateInput(attrs={'type': 'date'}),
    }