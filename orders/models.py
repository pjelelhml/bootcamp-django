from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product
# Create your models here.


User = get_user_model()

ODER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('stale', 'Stale'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),

)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=20, choices=ODER_STATUS_CHOICES, default='created')
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    tax = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    shipping_address = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
