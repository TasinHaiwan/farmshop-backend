from django.urls import path
from . import views

urlpatterns = [
    #HTML Pages
    path("shops/browse/", views.shops_page, name="shops-page"),
    path("shops/<int:pk>/browse/", views.shop_detail_page, name="shop-detail-page"),
    path("items/browse", views.items_page, name="items-page"),
    path("items/<int:pk>/browse/", views.item_detail_page, name="item-detail-page"),
    path("categories/browse/", views.categories_page, name="categories-page"),

    # API
    path("api/categories/", views.FoodCategoryListView.as_view(), name="category-list"),

    path("api/shops/", views.ShopListView.as_view(), name="shop-list"),
    path("api/shops/<int:pk>/", views.ShopDetailView.as_view(), name="shop-detail"),
    path("api/shops/<int:shop_id>/items/", views.ShopItemListView.as_view(), name="shop-items"),

    path("api/items/", views.FoodItemListView.as_view(), name="item-list"),
    path("api/items/<int:pk>/", views.FoodItemDetailView.as_view(), name="item-detail"),
]
