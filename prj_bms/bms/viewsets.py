from django.shortcuts import render
from .models import Category, Brand 
from .models import Shop
from rest_framework import viewsets, filters
from .serializers import CategorySerializer, BrandSerializer, ShopSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('category_id')
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_id', 'category_name', 'category_description')


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer