from rest_framework import serializers
from .models import FoodCategory, Shop, FoodItem


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ["id", "name", "emoji"]


class FoodItemSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source="shop.name", read_only=True)

    class Meta:
        model = FoodItem
        fields = [
            "id",
            "name",
            "shop_name",
            "unit",
            "price",
            "rating",
            "is_organic",
            "emoji",
            "color_hex",
        ]


class ShopSerializer(serializers.ModelSerializer):
    items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "tag",
            "rating",
            "review_count",
            "delivery_time",
            "delivery_fee",
            "is_open",
            "emoji",
            "color_hex",
            "items",
        ]


class ShopListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for list views (no items)."""

    class Meta:
        model = Shop
        fields = [
            "id",
            "name",
            "tag",
            "rating",
            "review_count",
            "delivery_time",
            "delivery_fee",
            "is_open",
            "emoji",
            "color_hex",
        ]
