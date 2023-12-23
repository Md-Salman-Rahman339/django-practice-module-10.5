from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('add/', views.add_post, name='add_post'),
    path('add/', views.AddPostCreateView.as_view(), name='add_post'),
    path('edit/<int:id>', views.EditPOstView.as_view(), name='edit_post'),
    path('delete/<int:id>', views.DeletePOstView.as_view(), name='delete_post'),
    path('details/<int:id>', views.DetailPostView.as_view(), name='detail_post')
]