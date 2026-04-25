from django.contrib import admin
from .models import FoodCategory, Shop, FoodItem


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "emoji"]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "tag", "rating", "is_open", "delivery_fee"]
    list_filter = ["is_open"]
    search_fields = ["name", "tag"]


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "shop", "unit", "price", "rating", "is_organic"]
    list_filter = ["is_organic", "shop"]
    search_fields = ["name", "shop__name"]
