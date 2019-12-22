from django.db import models
from django.conf import settings
from mainapp.models import Product

class BasketSlot(models.Model):
    class Meta:
        verbose_name = 'Слот корзины'
        verbose_name_plural = 'Слоты корзины'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    add_datatime = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}' #'{} - {}'.format(self.user.username, self.product.name)