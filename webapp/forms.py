from django import forms
from decimal import Decimal
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Наименование категории',
            'description': 'Описание',
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'stock', 'image']
        labels = {
            'name': 'Наименование товара',
            'description': 'Описание',
            'category': 'Категория',
            'price': 'Стоимость',
            'stock': 'Остаток на складе',
            'image': 'Ссылка на изображение',
        }
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        if price >= Decimal('100000.00'):
            raise forms.ValidationError("Максимальная цена: 99999.99")
        return price
