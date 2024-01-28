from django.contrib import admin
from .models import Product, Order, User


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'quantity']
    ordering = ['price']
    list_filter = ['quantity']
    search_fields = ['product']
    search_help_text = 'Поиск продукта'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price', 'date_ordered']
    ordering = ['date_ordered']
    list_filter = ['total_price']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по дате'
    readonly_fields = ['client', 'date_ordered']
    fieldsets = [
        (
            'Клиент',
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'Продукты',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['products', 'total_price'],
            },
        ),
        (
            'Дата заказа',
            {
                'fields': ['date_ordered'],

            }
        ),
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'register_date']
    ordering = ['name']
    list_filter = ['address']
    search_fields = ['name']
    search_help_text = 'Поиск по имени'

    readonly_fields = ['register_date', 'name']
    fieldsets = [
        (
            'Пользователь',
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Контактная информация',
            {
                'classes': ['collapse', 'wide'],
                'fields': ['phone', 'address', 'email'],
            },
        ),
        (
            'Дата регистрации',
            {
                'fields': ['register_date'],

            }
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
