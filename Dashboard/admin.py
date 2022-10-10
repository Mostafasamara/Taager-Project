from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','phone_number','Addres']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','real_price','sell_price','commission','available', 'created', 'updated','status','link']


@admin.register(Orders)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user','product','status']
