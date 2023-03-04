from django.db import models
from django.contrib.auth.models import User
from apps.shop.models import Item


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошик'
        db_table = 'cart'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    cart = models.ManyToManyField(Cart)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Загалом')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=255, verbose_name='Коментар', null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        db_table = 'order'
