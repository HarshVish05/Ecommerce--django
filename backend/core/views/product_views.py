from django.shortcuts import render
from django.http import JsonResponse

# rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from core.models import Product
from core.serializers import ProductSerializer

# for hashing the password
from django.contrib.auth.hashers import make_password



# django rest framework
@api_view(['GET']) # WRITE THE NAME OF THE METHODS YOU WANNA CALL 
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)  # many means we will serialize multiple objects
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id = pk)
    serializer = ProductSerializer(product, many = False)

    return  Response(serializer.data)     


# def getRoutes(request):
#     return JsonResponse('hello', safe=False)
"""By default, Django expects the data passed to JsonResponse to be a dictionary 
(i.e., a JSON object). If you pass a type other than a dictionary (such as a list or a string), 
Django will raise an error unless you set safe=False.
"""