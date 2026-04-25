"""
Management command to seed the database with the initial data
that previously lived in Flutter's static constants.

Usage:
    python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from shop.models import FoodCategory, Shop, FoodItem


CATEGORIES = [
    {"name": "All", "emoji": "🌿"},
    {"name": "Fruits", "emoji": "🍎"},
    {"name": "Vegetables", "emoji": "🥦"},
    {"name": "Dairy", "emoji": "🥛"},
    {"name": "Honey", "emoji": "🍯"},
    {"name": "Grains", "emoji": "🌾"},
    {"name": "Herbs", "emoji": "🌱"},
    {"name": "Nuts", "emoji": "🥜"},
]

SHOPS = [
    {
        "name": "Green Harvest Farm",
        "tag": "Organic · Vegetables · Fruits",
        "rating": 4.9,
        "review_count": 312,
        "delivery_time": "25-35 min",
        "delivery_fee": "৳30",
        "is_open": True,
        "emoji": "🌿",
        "color_hex": "2D6A4F",
        "items": [
            {"name": "Heirloom Tomatoes", "unit": "500g", "price": 85, "rating": 4.9, "is_organic": True,  "emoji": "🍅", "color_hex": "E85D4A"},
            {"name": "Baby Spinach",      "unit": "250g", "price": 65, "rating": 4.8, "is_organic": True,  "emoji": "🥬", "color_hex": "52B788"},
            {"name": "Golden Carrots",    "unit": "1kg",  "price": 70, "rating": 4.7, "is_organic": True,  "emoji": "🥕", "color_hex": "F4A261"},
            {"name": "Strawberries",      "unit": "400g", "price": 120,"rating": 4.9, "is_organic": False, "emoji": "🍓", "color_hex": "E63946"},
            {"name": "Bell Peppers Mix",  "unit": "3 pcs","price": 90, "rating": 4.6, "is_organic": True,  "emoji": "🫑", "color_hex": "2DC653"},
            {"name": "Eggplant",          "unit": "2 pcs","price": 55, "rating": 4.5, "is_organic": True,  "emoji": "🍆", "color_hex": "7B2FBE"},
        ],
    },
    {
        "name": "Sunflower Organics",
        "tag": "Dairy · Honey · Herbs",
        "rating": 4.7,
        "review_count": 198,
        "delivery_time": "30-45 min",
        "delivery_fee": "৳25",
        "is_open": True,
        "emoji": "🌻",
        "color_hex": "D4A017",
        "items": [
            {"name": "Raw Wildflower Honey", "unit": "500ml", "price": 350, "rating": 5.0, "is_organic": True, "emoji": "🍯", "color_hex": "D4A017"},
            {"name": "Full-Fat Yogurt",      "unit": "400g",  "price": 110, "rating": 4.8, "is_organic": True, "emoji": "🥛", "color_hex": "F0EDE8"},
            {"name": "Fresh Basil",          "unit": "bunch", "price": 45,  "rating": 4.7, "is_organic": True, "emoji": "🌿", "color_hex": "52B788"},
        ],
    },
    {
        "name": "Nature's Basket",
        "tag": "Nuts · Grains · Dried Fruits",
        "rating": 4.8,
        "review_count": 245,
        "delivery_time": "20-30 min",
        "delivery_fee": "Free",
        "is_open": False,
        "emoji": "🧺",
        "color_hex": "8B5E3C",
        "items": [],
    },
    {
        "name": "Pure Roots",
        "tag": "Roots · Tubers · Spices",
        "rating": 4.6,
        "review_count": 130,
        "delivery_time": "35-50 min",
        "delivery_fee": "৳20",
        "is_open": True,
        "emoji": "🫚",
        "color_hex": "C45C26",
        "items": [],
    },
]


class Command(BaseCommand):
    help = "Seed initial data (categories, shops, items)"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding categories...")
        for cat in CATEGORIES:
            FoodCategory.objects.get_or_create(name=cat["name"], defaults={"emoji": cat["emoji"]})

        self.stdout.write("Seeding shops and items...")
        for shop_data in SHOPS:
            items = shop_data.pop("items")
            shop, _ = Shop.objects.get_or_create(
                name=shop_data["name"], defaults=shop_data
            )
            for item_data in items:
                FoodItem.objects.get_or_create(
                    shop=shop, name=item_data["name"], defaults=item_data
                )

        self.stdout.write(self.style.SUCCESS("Done! Database seeded successfully."))
