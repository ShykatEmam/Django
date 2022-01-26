import pstats
from django.contrib import admin
from .models import Feature
from .models import ShoppingMalls

# Register your models here.
class FeatureAdmin(admin.ModelAdmin):pass

admin.site.register(Feature)

@admin.register(ShoppingMalls)
class ShoppingMalls(admin.ModelAdmin):
    pass