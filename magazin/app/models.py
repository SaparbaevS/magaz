from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Magazin(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    price = models.PositiveIntegerField()
    status = models.BooleanField()
    date_of_purchase = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.price}'

    def get_absolute_url(self):
        return reverse("users:detail", args=(self.slug, ))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)