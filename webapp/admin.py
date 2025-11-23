from django.contrib import admin
from webapp.models import (
    Category,
    Product,
    CartProduct,
    Order,
    OrderProduct
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "created_at", "stock")
    list_filter = ("category",)
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(CartProduct)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity")
    list_filter = ("product",)
    ordering = ("id",)


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone", "address", "created_at")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    inlines = [OrderProductInline]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity")
    list_filter = ("order", "product")
    ordering = ("id",)
