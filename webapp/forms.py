from django import forms
from webapp.models import Product
from webapp.models import Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "price", "stock", "image"]

    def clean_stock(self):
        stock = self.cleaned_data.get("stock")
        if stock < 0:
            raise forms.ValidationError("Остаток не может быть меньше 0.")
        return stock

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["username", "phone", "address"]