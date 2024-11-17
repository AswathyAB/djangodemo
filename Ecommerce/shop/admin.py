from django.contrib import admin
from shop.models import Itemcategory
from shop.models import Product
# Register your models here.
admin.site.register(Itemcategory)
admin.site.register(Product)