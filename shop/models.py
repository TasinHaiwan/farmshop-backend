from django.db import models


class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
    emoji = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Food Categories"

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    tag = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review_count = models.PositiveIntegerField(default=0)
    delivery_time = models.CharField(max_length=50)   # e.g. "25-35 min"
    delivery_fee = models.CharField(max_length=50)    # e.g. "৳30" or "Free"
    is_open = models.BooleanField(default=True)
    emoji = models.CharField(max_length=10)
    color_hex = models.CharField(max_length=6)        # e.g. "2D6A4F" (no #)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)            # e.g. "500g", "bunch"
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    is_organic = models.BooleanField(default=False)
    emoji = models.CharField(max_length=10)
    color_hex = models.CharField(max_length=6)        # e.g. "E85D4A" (no #)

    def __str__(self):
        return f"{self.name} ({self.shop.name})"
