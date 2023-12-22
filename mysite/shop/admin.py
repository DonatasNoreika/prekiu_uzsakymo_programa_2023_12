from django.contrib import admin
from .models import Status, Product, Order, OrderLine

class OrderLineInLine(admin.TabularInline):
    model = OrderLine
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", 'date', 'status']
    inlines = [OrderLineInLine]

# Register your models here.
admin.site.register(Status)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
