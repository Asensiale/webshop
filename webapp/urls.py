from django.urls import path
from webapp.views import (
    ProductListView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    cart_add, cart_view, cart_delete, cart_remove_one, create_order
)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    path("add/", ProductCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", ProductUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
    path("cart/", cart_view, name="cart"),
    path("cart/add/<int:pk>/", cart_add, name="add"),
    path("cart/delete/<int:pk>/", cart_delete, name="cart_delete"),
    path("cart/remove_one/<int:pk>/", cart_remove_one, name="remove_one"),
    path("order/create/", create_order, name="order_create"),
]

