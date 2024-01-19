from django.contrib import admin
from .apps.models import Product, Transaction

admin.site.register(Product)
admin.site.register(Transaction)
