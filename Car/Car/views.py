from django.shortcuts import render, get_object_or_404
from car_model.models import Car
from brand_model.models import Brand

def home(request, brand_slug=None):
    data = Car.objects.all()
    brands = Brand.objects.all()

    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        data = Car.objects.filter(brand=brand)
    else:
        brand = None 

    return render(request, 'home.html', {'data': data,'brand': brand,'brands':brands})
