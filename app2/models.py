import uuid
from django.db import models
from django.db.models import Model

# Create your models here.
class Feature(models.Model):
    name: models.CharField(max_length=100)
    details: models.CharField(max_length=500)
    def __str__(self):
        return self.name
class ShoppingMalls(models.Model):
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