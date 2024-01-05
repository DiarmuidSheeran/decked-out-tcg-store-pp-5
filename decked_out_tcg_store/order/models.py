from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):

    SHIPPING_STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('in_process', 'In Process'),
        ('shipped', 'Shipped'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True)
    email_address = models.CharField(max_length=200, null=True)
    shipping_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shipping_status = models.CharField(max_length=20, choices=SHIPPING_STATUS_CHOICES, default='ordered')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.get_shipping_status_display()}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.pk}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.quantity_available -= self.quantity
        self.product.save()

