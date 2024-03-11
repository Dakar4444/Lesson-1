from django.contrib import admin
from .models import User, Product, Order

# Register your models here.

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ['name', 'email', 'date_of_registration']
    list_filter = ['date_of_registration']
    search_fields = ['name']
    list_editable = ['email']
    ordering = ['name']
    list_per_page = 10
    fieldsets = [
        ('Personal info',{
            'fields': ['name', 'date_of_registration'],
            'description': 'Information about User',
            'classes': ['collapse']
        }),
        ('Contact',{
            'fields': ['phone_number', 'adress', 'email'],
            'classes': ['collapse']
        }),
    ]



@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'date_of_addition']
    list_filter = ['price', 'date_of_addition']
    search_fields = ['name']
    ordering = ['name']
    list_per_page = 10
    fieldsets = [
        ('Info',{
            'fields': ['name', 'price', 'quantity', 'date_of_addition'],
        }),
        ('Description',{
            'fields': ['description'],
            'classes': ['collapse']
        }),
        ('Image',{
            'fields': ['image']
        }),
    ]


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_price','date_order']
    list_filter = ['total_price', 'date_order']
    search_fields = ['customer', 'products']
    list_per_page = 10
    readonly_fields = ['date_order']
    ordering = ['id']
    fieldsets = [
        ('Info',{
            'fields': ['customer', 'date_order'],
        }),
        ('Products',{
            'fields': ['products', 'total_price'],
            'classes': ['collapse']
        }),
    ]