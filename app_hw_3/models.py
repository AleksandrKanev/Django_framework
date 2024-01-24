from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone = models.IntegerField(null=True)
    address = models.CharField(null=True, max_length=100)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Имя: {self.name}, телефон: {self.phone}'


# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара

class Product(models.Model):
    product = models.CharField(max_length=100)
    info = models.CharField(null=True, max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    quantity = models.IntegerField(default=1)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.product}, price: {self.price}'


# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары,
# входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order: {self.pk} Client: {self.client.name}, total_price: {self.total_price}'
