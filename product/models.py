from django.db import models
from category.models import Category
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=500, default='This is a product that many people love in 2022.')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='product_images/', blank=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created  = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    # Khi ban muon lay url, phai khai bao them app_name trong urls.py
    # va truyen nhu ben duoi "app_name:view_name"
    def get_absolute_url(self):
        return reverse("my_app:product_detail", kwargs={"slug": self.slug})  # new