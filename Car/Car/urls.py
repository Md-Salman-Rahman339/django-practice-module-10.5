from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('brand_model/<slug:brand_slug>/',views.home,name='brand_wise_post'),
    path('brand_model/',include('brand_model.urls')),
    path('car_model/',include('car_model.urls')),
    path('owner/',include('owner.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)