from django.db import models
from musician.models import Musician

class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    ratings = models.IntegerField(choices=CHOICES, default=1)

    release_date = models.DateField()

    def __str__(self):
        return self.album_name
