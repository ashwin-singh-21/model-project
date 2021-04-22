from django.contrib import admin

# Register your models here.

from .models import mymodel,Product,orders,Tag

admin.site.register(mymodel)
admin.site.register(Product)
admin.site.register(orders)
admin.site.register(Tag)