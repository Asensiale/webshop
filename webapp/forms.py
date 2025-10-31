from django import forms
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
        fields = ['name', 'description', 'category', 'price', 'image']
        labels = {
            'name': 'Наименование товара',
            'description': 'Описание',
            'category': 'Категория',
            'price': 'Стоимость',
            'image': 'Ссылка на изображение',
        }
