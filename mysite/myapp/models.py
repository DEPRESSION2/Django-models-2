from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _

#User = get_user_model()
# Create your models here.


class Customer(AbstractUser):

    wallet = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Кошелёк', default=10000)


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение', null=True)
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title


 class Purchase(models.Model):
     user = models.ForeignKey('Customer', on_delete=models.CASCADE)
   product = models.ForeignKey('Product', on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    qty = models.PositiveIntegerField(default=1)
     created = models.DateTimeField(auto_now_add=True)


 class Return(models.Model):
     purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
     created = models.DateTimeField(auto_now_add=True)






