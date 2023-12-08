from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='HomePage'),
    path('about/',views.about,name='About'),
    path('form/',views.submit_form,name='Submit_form'),
    path('django_form',views.StudentForm,name="django_form")
    
    
    
]
