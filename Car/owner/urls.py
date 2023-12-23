from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('pass_change/',views.pass_change,name='passchange'),
]
