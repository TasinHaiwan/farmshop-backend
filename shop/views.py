from django.shortcuts import render
from rest_framework import generics, filters
from .models import FoodCategory, Shop, FoodItem
from .serializers import (
    FoodCategorySerializer,
    FoodItemSerializer,
    ShopSerializer,
    ShopListSerializer,
)

# HTML Template Views

def shops_page(request):
    return render(request, 'shop/shops.html')

def shop_detail_page(request, pk):
    return render(request, 'shop/shop_detail.html')

def items_page(request):
    return render(request, 'shop/items.html')

def item_detail_page(request, pk):
    return render(request, 'shop/item_detail.html')

def categories_page(request):
    return render(request, 'shop/categories.html')

# API Views

class FoodCategoryListView(generics.ListAPIView):
    """GET /api/categories/ — all food categories"""
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer


class ShopListView(generics.ListAPIView):
    """GET /api/shops/ — all shops (no items embedded)"""
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "tag"]


class ShopDetailView(generics.RetrieveAPIView):
    """GET /api/shops/<id>/ — single shop with all its items"""
    queryset = Shop.objects.prefetch_related("items")
    serializer_class = ShopSerializer


class ShopItemListView(generics.ListAPIView):
    """GET /api/shops/<shop_id>/items/ — items for a specific shop"""
    serializer_class = FoodItemSerializer

    def get_queryset(self):
        return FoodItem.objects.filter(shop_id=self.kwargs["shop_id"])


class FoodItemListView(generics.ListAPIView):
    """GET /api/items/ — all items, optionally filtered by ?is_organic=true"""
    serializer_class = FoodItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        qs = FoodItem.objects.select_related("shop").all()
        is_organic = self.request.query_params.get("is_organic")
        if is_organic is not None:
            qs = qs.filter(is_organic=is_organic.lower() == "true")
        return qs


class FoodItemDetailView(generics.RetrieveAPIView):
    """GET /api/items/<id>/"""
    queryset = FoodItem.objects.select_related("shop")
    serializer_class = FoodItemSerializer
