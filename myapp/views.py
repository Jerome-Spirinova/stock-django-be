from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, UpdateStockSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    
class ExpensiveProductView(APIView):
    def get(self, request, *args, **kwargs):
        expensive_product = Product.objects.order_by('-price').first()
        if expensive_product:
            serializer = ProductSerializer(expensive_product)
            return Response(serializer.data)
        return Response({"detail": "No products available"}, status=404)
    
class FeaturedProductView(APIView):
    def get(self, request, *args, **kwargs):
        featured_product = Product.objects.order_by('-stocks').first()
        if featured_product:
            serializer = ProductSerializer(featured_product)
            return Response(serializer.data)
        return Response({"detail": "No products available"}, status=404)
    
class UpdateStockView(APIView):
    @swagger_auto_schema(
        request_body=UpdateStockSerializer,
        responses={
            200: openapi.Response('Stock updated successfully'),
            404: openapi.Response('Product not found'),
            400: openapi.Response('Invalid input')
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = UpdateStockSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product_id']
            stocks = serializer.validated_data['stocks']
            try:
                product = Product.objects.get(id=product_id)
                product.stocks = stocks
                product.save()
                return Response({"detail": "Stock updated successfully"}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)