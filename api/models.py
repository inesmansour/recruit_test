from django.db import models
import uuid


class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, blank=False)

    class Meta:
        ordering = ('name', '-date_changed')


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=50, blank=False)
    price_EUR_per_kg = models.FloatField(blank=False)
    
    class Meta:
        ordering = ('name', '-date_changed')


class PricingLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pricing_history')
    price_EUR_per_kg = models.FloatField(blank=False)

    class Meta:
        ordering = ('-date_created',)
