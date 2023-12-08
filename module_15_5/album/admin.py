from django.contrib import admin

from . import models
from .models import Album


# Register your models here.
admin.site.register(models.Album)

