from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'email', 'total_paid', 'billing_status', 'created']
    list_filter = ['billing_status', 'created']
    search_fields = ['full_name', 'email', 'order_key']
    
    inlines = [OrderItemInline]
    
    readonly_fields = ['created', 'order_key']