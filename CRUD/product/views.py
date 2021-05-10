from django.shortcuts import render, redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import productSerializer
from .models import product

from rest_framework.exceptions import NotFound


@api_view(['GET'])
def productOverview(request):
    product_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create': '/product-create/',
        'Update': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>/'
    }
    return Response(product_urls)

@api_view(['GET'])
def productList(request):
    products = product.objects.all()
    serializer = productSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
    products = product.objects.get(id=pk)
    serializer = productSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = productSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
def productUpdate(request, pk):
    products = product.objects.get(id=pk)
    serializer = productSerializer(instance=products, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
    try:
        product = product.objects.get(id=pk)
        product.delete()
        return Response("Product deleted successfully!")
    except product.DoesNotExist:
        raise NotFound(detail="Error 404, ID not found", code=404)


