from django.urls import path

from .views import getRoutes,getProducts, getProduct

app_name = 'core'

urlpatterns = [
    path('', getRoutes, name="getroute"),
    path('products', getProducts, name="products"),
    path('products/<str:pk>/', getProduct, name="product"),
]
