from django.contrib import admin
from .models import Feature

# Register your models here.
class FeatureAdmin(admin.ModelAdmin):pass

admin.site.register(Feature)