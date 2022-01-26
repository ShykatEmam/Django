import uuid
from django.db import models
from django.db.models import Model

# Create your models here.
class Test(models.Model):
  #owner
    title_new = models.CharField(max_length=200)
    description = models.TextField(null=False)
    division = models.CharField(max_length=200)
    address = models.TextField(null=False)
    
    category_1 = models.CharField(max_length=200)
    category_2 = models.CharField(max_length=200)
    category_3 = models.CharField(max_length=200)
    category_4 = models.CharField(max_length=200)
    category_5 = models.CharField(max_length=200)
    category_6 = models.CharField(max_length=200)
    category_7 = models.CharField(max_length=200)
    # featured_image
    website_link = models.CharField(max_length=1000)
    facebook_link = models.CharField(max_length=1000)
    other_link = models.CharField(max_length=1000)
    
    division = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
class Feature(models.Model):
    name: models.CharField(max_length=100)
    details: models.CharField(max_length=500)
    def __str__(self):
        return self.name
class ShoppingMalls(models.Model):
   #owner
    title_new = models.CharField(max_length=200)
    description = models.TextField(null=False)
    division = models.CharField(max_length=200)
    address = models.TextField(null=False)
    
    category_1 = models.CharField(max_length=200,null=True,blank=True)
    category_2 = models.CharField(max_length=200,null=True,blank=True)
    category_3 = models.CharField(max_length=200,null=True,blank=True)
    category_4 = models.CharField(max_length=200,null=True,blank=True)
    category_5 = models.CharField(max_length=200,null=True,blank=True)
    category_6 = models.CharField(max_length=200,null=True,blank=True)
    category_7 = models.CharField(max_length=200,null=True,blank=True)
    # featured_image
    website_link = models.CharField(max_length=1000,null=True,blank=True)
    facebook_link = models.CharField(max_length=1000,null=True,blank=True)
    other_link = models.CharField(max_length=1000,null=True,blank=True)
    
    division = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/',null=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

class Product(models.Model):
    #owner
    title = models.CharField(max_length=200)
    description = models.TextField(null=False)
    # featured_image
    demo_link = models.CharField(max_length=1000)
    source_link = models.CharField(max_length=1000)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)