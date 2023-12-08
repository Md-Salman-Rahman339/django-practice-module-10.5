from django.db import models

# Create your models here.

class Musician(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    email=models.EmailField()
    Phone=models.CharField(max_length=13)
    instrument_type=models.CharField(max_length=9)


    def __str__(self):
        return self.First_name

