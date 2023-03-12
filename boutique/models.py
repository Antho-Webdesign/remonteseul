from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    img_cat = models.ImageField(upload_to='category', blank=True, null=True, default='default.jpg')

    def __str__(self):
        return self.name

