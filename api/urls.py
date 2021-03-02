from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('users', views.UserViewSet, basename='users')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('storages', views.StorageViewSet, basename='storages')
router.register('stores', views.StoreViewSet, basename='stores')

