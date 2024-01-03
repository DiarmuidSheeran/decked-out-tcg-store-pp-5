from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'display_categories', 'quantity_available', 'is_featured', 'created_at', 'updated_at']
    search_fields = ['name', 'categories__name']
    list_filter = ['categories', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}

    def display_categories(self, obj):
        return ', '.join(category.name for category in obj.categories.all())

    display_categories.short_description = 'Categories'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
