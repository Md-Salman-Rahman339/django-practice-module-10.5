from django.db import models
from django.contrib.auth.models import User
from brand_model.models import Brand


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    car_model_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_model/media/uploads', blank=True, null=True)
    car_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description=models.TextField(max_length=255, default='Some default value')
    quantity=models.PositiveIntegerField(default=0)




    def __str__(self):
        return f"{self.car_model_name} ({self.brand})"


class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"

class BuyCar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return f"buy this car name: {self.car.Name}"