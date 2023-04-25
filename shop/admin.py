from django.contrib import admin
from .models import products
from .models import Contacts

# Register your models here.

admin.site.register(products)
admin.site.register(Contacts)
