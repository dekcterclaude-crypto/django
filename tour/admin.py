from django.contrib import admin
from . import models
from .models import Tour, Category, Person, Comment

admin.site.register(models.Tour)
admin.site.register(models.Category)
admin.site.register(models.Person)
admin.site.register(models.Comment)

