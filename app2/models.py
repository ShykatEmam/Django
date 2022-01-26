from django.db import models
from django.db.models import Model

# Create your models here.
class Feature(models.Model):
    name: models.CharField(max_length=100)
    details: models.CharField(max_length=500)
    
    def __str__(self):
        return self.name
        

class ShoppingMalls(models.Model):
    mallname: models.TextField(max_length=100)
    product1: models.CharField(max_length=75)
    product2: models.CharField(max_length=75)
    product3: models.CharField(max_length=75)
    product4: models.CharField(max_length=75)
    product5: models.CharField(max_length=75)
    product6: models.CharField(max_length=75)
    product7: models.CharField(max_length=75)
    link1: models.URLField(max_length=200)
    link2: models.URLField(max_length=200)
    link3: models.EmailField(max_length=100)
    link4: models.URLField(max_length=200)
    division: models.CharField(max_length=50)
    location: models.URLField(max_length=200)
    images: models.ImageField(upload_to='upload_to/')
    mall_description: models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name