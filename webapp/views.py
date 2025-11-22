from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.db.models import Q
from webapp.models import Product
from webapp.forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        queryset = Product.objects.filter(amount__gte=1)
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
