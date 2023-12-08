from django.urls import path
from .views import StudentForm

urlpatterns = [
    path('django_form/', StudentForm, name='student_form'),
   
]
