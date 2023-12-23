from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    instrument_type = models.CharField(max_length=9)

    def __str__(self):
        return self.first_name
