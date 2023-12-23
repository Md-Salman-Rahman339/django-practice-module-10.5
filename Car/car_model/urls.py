from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.AddPostCreateView.as_view(), name='add_post'),
    path('car_model/details/<int:id>/', views.DetailsPost.as_view(), name='detail_post'), 
    path('buy_car/<int:id>/', views.buy_car, name='buy_car'),
    # path('details/<int:id>/', views.detail_post_view, name='detail_post_view'),
]
