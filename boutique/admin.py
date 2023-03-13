from django.contrib import admin

from boutique.models import Category, Device, Marques, Tutorial

# Register your models here.
admin.site.register(Category)
admin.site.register(Device)
admin.site.register(Marques)
admin.site.register(Tutorial)
