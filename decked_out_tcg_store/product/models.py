from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    quantity_available = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    on_special_offer = models.BooleanField(default=False)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
