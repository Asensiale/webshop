from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from webapp.models import Product, CartProduct, OrderProduct
from webapp.forms import ProductForm, OrderForm


class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        queryset = Product.objects.filter(stock__gte=1)
        search = self.request.GET.get("q", "")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search)
            )
        return queryset.order_by("category__name", "name")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("products:list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("products:list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("products:list")


def cart_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    quantity = int(request.POST.get("quantity", 1))

    if product.stock < 1 or quantity < 1:
        return redirect(request.META.get("HTTP_REFERER", "products:list"))

    cart_item, created = CartProduct.objects.get_or_create(product=product)

    if created:
        if quantity <= product.stock:
            cart_item.quantity = quantity
            cart_item.save()
    else:
        if cart_item.quantity + quantity <= product.stock:
            cart_item.quantity += quantity
            cart_item.save()

    return redirect(request.META.get("HTTP_REFERER", "products:list"))


def cart_remove_one(request, pk):
    item = get_object_or_404(CartProduct, pk=pk)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    referer = request.META.get("HTTP_REFERER")
    return redirect(referer or "products:cart")


def cart_view(request):
    cart_items = CartProduct.objects.all()
    total_sum = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_sum": total_sum,
    }

    return render(request, "cart.html", context)


def cart_delete(request, pk):
    item = get_object_or_404(CartProduct, pk=pk)
    item.delete()


    return redirect("products:cart")


def create_order(request):
    cart_items = CartProduct.objects.all()

    if not cart_items:
        return redirect("products:cart")

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()


            for item in cart_items:
                OrderProduct.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )


            cart_items.delete()

            return redirect("products:list")
    else:
        form = OrderForm()

    return render(request, "order_create.html", {"form": form})
