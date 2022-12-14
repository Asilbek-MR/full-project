from django.db import models
from apps.product.models import Product
from django.conf import settings

User=settings.AUTH_USER_MODEL


class Card(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    total_items=models.IntegerField(default=0)


class CardItem(models.Model):
    card=models.ForeignKey(Card, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    count=models.IntegerField()















