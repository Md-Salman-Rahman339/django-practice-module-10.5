from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.MusicianView.as_view(), name='musician'),
    path('musician/edit/<int:id>/', views.edit_musician, name='edit_musician'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]
