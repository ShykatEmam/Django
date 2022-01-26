
from django.contrib import admin
from .models import Feature
from .models import ShoppingMalls
from .models import Product

# Register your models here.
admin.site.register(Product)
class FeatureAdmin(admin.ModelAdmin):pass

admin.site.register(Feature)

admin.site.register(ShoppingMalls)