
from django.db import models


class Electronics(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара', blank=True)
    CHEKING = (
        ('В наличии✅', 'В наличии✅'),
        ('Под заказ⏳', 'Под заказ⏳'),
        ('Нет в наличии🚫', 'Нет в наличии🚫')
    )

    cheking = models.CharField(
        max_length=100,
        default='Нет в наличии🚫',
        choices=CHEKING,
        verbose_name='Выберите статус'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
