from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('populate', views.debug_populate)
]
