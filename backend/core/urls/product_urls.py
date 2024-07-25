from django.urls import path

from core.views.product_views import getProducts, getProduct

app_name = 'core'

urlpatterns = [
    path('', getProducts, name="products"),
    path('<str:pk>/', getProduct, name="product"),
]
