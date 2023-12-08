from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.musician,name='musician'),
    path('musician/edit/<int:id>/',views.edit_musician,name='edit_musician'),
   

    
]
