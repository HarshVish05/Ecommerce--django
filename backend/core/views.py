from django.shortcuts import render
from django.http import JsonResponse

# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products

def getRoutes(request):
    return JsonResponse('hello', safe=False)
    """By default, Django expects the data passed to JsonResponse to be a dictionary 
    (i.e., a JSON object). If you pass a type other than a dictionary (such as a list or a string), 
    Django will raise an error unless you set safe=False.
    """

# django rest framework
@api_view(['GET']) # WRITE THE NAME OF THE METHODS YOU WANNA CALL 
def getProducts(request):
    return Response(products)

@api_view(['GET'])
def getProduct(request, pk):
    for product in products:
        if product['_id'] == pk:
            return Response(product)

    return  Response('Not Found')     
