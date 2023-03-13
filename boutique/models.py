from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    description = models.TextField(blank=True, null=True)
    img_cat = models.ImageField(upload_to='category', blank=True, null=True, default='default.jpg')

    def __str__(self):
        return self.name


class Marques(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    description = models.TextField(null=True)
    logo = models.ImageField(upload_to='marques/', null=True, blank=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    marque = models.ForeignKey(Marques, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='devices/', null=True, blank=True)

    def __str__(self):
        return self.name


class Appareils(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    marque = models.ForeignKey(Marques, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='devices/', null=True, blank=True)

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    appareil = models.ForeignKey(Appareils, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=255)
    description = models.TextField(null=True)
    duration = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='tutorials/', null=True, blank=True)

    def __str__(self):
        return self.title


class Guide(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)
    appareil = models.ForeignKey(Appareils, on_delete=models.CASCADE, null=True)
    author = models.CharField(max_length=255)
    description = models.TextField()
    format = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='guides/')

    def __str__(self):
        return self.title
