from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='category_images/',blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("my_app:category", kwargs={"slug": self.slug})  # new
    