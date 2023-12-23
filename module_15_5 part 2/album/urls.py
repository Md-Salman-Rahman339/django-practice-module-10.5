# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('album/', views.AddAlbumCreateView.as_view(), name='album'),
    path('album/edit/<int:id>/', views.EditAlbumView.as_view(), name='edit_album'),
    path('delete_album/<int:id>/', views.DeleteAlbumView.as_view(), name='delete_album'),
]
