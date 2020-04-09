from django.db import models
from django.conf import settings
from mainapp.models import Product


class BasketManagerQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super().delete()


class BasketSlot(models.Model):
    objects = BasketManagerQuerySet.as_manager()

    class Meta:
        verbose_name = 'Слот корзины'
        verbose_name_plural = 'Слоты корзины'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    add_datatime = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}' #'{} - {}'.format(self.user.username, self.product.name)

    def get_price(self):
        return self.quantity * self.product.price

    price = property(get_price)

    @classmethod
    def get_item(cls, pk):
        try:
            return cls.objects.get(pk=pk)
        except Exception as e:
            print(e)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()
