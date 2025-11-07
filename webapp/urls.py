from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.products_view, name='products-home'),
    path('products/', views.products_view, name='products-list'),
    path('products/add/', views.product_add_view, name='product-add'),
    path('categories/add/', views.category_add_view, name='category-add'),
    path('products/<int:id>/', views.product_detail_view, name='product-detail'),
    path('products/<int:id>/edit/', views.product_edit_view, name='product-edit'),       # редактирование
    path('products/<int:id>/delete/', views.product_delete_view, name='product-delete'), # удаление
]


