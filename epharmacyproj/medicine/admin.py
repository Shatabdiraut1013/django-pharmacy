from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Product,Cart,Customer,Contact,OrderPlaced
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'med_name', 'indications', 'dosage','side_effects','selling_price','category','product_image']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']    


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name',
                    'locality', 'city', 'zipcode', 'state']  

@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone','desc','date']      

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'customer_info',
                    'product', 'product_info', 'quantity', 'ordered_date', 'status']

    def customer_info(self, obj):
        # app is written in apps.py in name n customer is model name which we wriiten in models.py
        link = reverse("admin:medicine_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def product_info(self, obj):
        # app is written in apps.py in name n product is model name which we wriiten in models.py
        link = reverse("admin:medicine_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.med_name)
