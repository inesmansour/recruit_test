from api import models
from rest_framework import serializers

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ['url', 'name']


class ProductWithPricingHistorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SerializerMethodField()
    pricing_history = serializers.SerializerMethodField()
        
    def get_category(self, object:models.Product):
        return object.category.name
    
    def get_pricing_history(self, object:models.Product):
        return object.pricing_history.all().order_by('-date_created').values('date_created', 'price_EUR_per_kg')

    class Meta:
        model = models.Product
        fields = ['id','url', 'name', 'category', 'price_EUR_per_kg', 'date_created', 'date_changed', 'pricing_history']

class ProductCategoryWithProductsSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductWithPricingHistorySerializer(many=True)

    class Meta:
        model = models.ProductCategory
        fields = ['url', 'name', 'products']
