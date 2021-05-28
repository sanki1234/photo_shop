from photos.models import category, photo
from django.contrib import admin
from .models import category,photo

# Register your models here.
admin.site.register(category)
admin.site.register(photo)