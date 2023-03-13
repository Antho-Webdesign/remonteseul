from django.contrib import admin

from boutique.models import Category, Device, Marques, Tutorial, Appareils

# Register your models here.
admin.site.register(Category)
admin.site.register(Appareils)
admin.site.register(Marques)
admin.site.register(Tutorial)
