from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория"
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name="Стоимость"
    )
    image = models.URLField(verbose_name="Ссылка на изображение")
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="Остаток",
        help_text="Количество единиц товара на складе (не может быть меньше 0)"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

class CartProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

class Order(models.Model):
    username = models.CharField(max_length=100, verbose_name="Имя пользователя")
    phone = models.CharField(max_length=30, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заказ №{self.pk} от {self.username}"


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_products"
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Товар заказа"
        verbose_name_plural = "Товары заказа"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


