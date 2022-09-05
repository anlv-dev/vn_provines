from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","slug", "description", "price", "old_price", "category","stock","is_available", "image","created","modified")
    prepopulated_fields = {"slug": ("name",)} 

admin.site.register(Product, ProductAdmin)