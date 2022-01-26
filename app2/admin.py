
from django.contrib import admin
from .models import Feature, Test
from .models import ShoppingMalls
from .models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Test)
class FeatureAdmin(admin.ModelAdmin):pass

admin.site.register(Feature)

admin.site.register(ShoppingMalls)