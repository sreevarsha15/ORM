from django.db import models
from django.contrib import admin

class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()
    


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "Product_ID",
        "product_name",
        "brand",
        "category",
        "price",
        "description",
        "stock_quantity",
        "rating",
    ]


    
