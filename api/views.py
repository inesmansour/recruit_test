from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import ProductCategory, Product, PricingLog
from api import serializers

from django.utils import timezone
import random


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('-date_created')
    serializer_class = serializers.ProductWithPricingHistorySerializer

class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductCategory.objects.all().order_by('name')
    serializer_class = serializers.ProductCategoryWithProductsSerializer

@api_view()
def debug_populate(request):
    # NOTE: Bad practice business logic in view.
    # This is a minimal project, hence the shortcut.

    # Start by removing all: will cascade from Category -> Product -> Price Logs
    ProductCategory.objects.all().delete()

    clock = timezone.datetime(year=2020, month=5, day=12, hour=14, minute=30)

    # Create some random categories and products
    for catname in random.sample([
        'Apples', 'Apricots', 'Asparagus', 'Avocados', 'Cherries', 'Basil', 'Beets', 'Blackberries ', 'Blueberries',
        'Boysenberries', 'Broccoli', 'Cabbage ', 'Carrots ', 'Collards', 'Corn', 'Cucumber', 'Eggplants', 'Figs',
        'Grapes', 'Kale', 'Kohlrabi', 'Lemons', 'Lettuce', 'Melons', 'Mushrooms', 'Mustard', 'Nectarines',
        'Oranges', 'Okra ', 'Peaches', 'Peppers', 'Persimmons', 'Plums ', 'Potatoes', 'Raspberries', 'Sapote',
        'Spinach', 'Strawberries', 'Summer Squash', 'Tomatillos', 'Tomatoes', 'Turnips'
    ], k=5):
        category = ProductCategory.objects.create(name=catname)

        for prodtype in random.sample(['Superior', 'Extra', 'Regular', 'Organic', 'Prime', 'Fresh'], k=random.randint(1, 5)):
            prodname = '{0} {1}'.format(catname, prodtype)
            proddate = clock + timezone.timedelta(days=random.randint(1, 200), minutes=random.randint(0, 3600))
            prodprice = max(0.1, random.gauss(mu=5, sigma=2))

            product = Product.objects.create(
                category=category,
                name=prodname,
                price_EUR_per_kg=prodprice,
                date_created=proddate,
                date_changed=proddate
            )

            for _ in range(1, random.randint(2, 20)):
                proddate = proddate + timezone.timedelta(days=random.randint(1, 3), minutes=random.randint(0, 3600))
                PricingLog.objects.create(
                    date_created=proddate,
                    product=product,
                    price_EUR_per_kg=max(0.1, random.gauss(mu=prodprice, sigma=0.5))
                )
            
            product.date_changed = proddate
            product.save()

    return Response({'done': True})

