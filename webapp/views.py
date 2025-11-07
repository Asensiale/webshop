from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Product, Category
from webapp.forms import ProductForm, CategoryForm


def products_view(request):
    products = Product.objects.filter(stock__gte=1).order_by('category', 'name')
    return render(request, 'products.html', {'products': products})


def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})


def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-list')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})


def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products-list')
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})
def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-detail', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form, 'title': 'Редактирование товара'})


def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('products-list')
    return render(request, 'product_confirm_delete.html', {'product': product})
