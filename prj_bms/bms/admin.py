from django.contrib import admin

# Register your models here.
from .models import Category, Brand , Shop, Invoice, Quantity, Shift,BmsUser

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Shop)
admin.site.register(Invoice)
admin.site.register(Quantity)
admin.site.register(Shift)
admin.site.register(BmsUser)

