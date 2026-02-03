from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'in_stock', 'is_active', 'created', 'updated']
    list_filter = ['in_stock', 'is_active', 'category']
    list_editable = ['price', 'in_stock', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20