from django.contrib import admin
from .models import Feature
from .models import Malls
from .models import Product

# Register your models here.
admin.site.register(Product)
class MallsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Malls, MallsAdmin)