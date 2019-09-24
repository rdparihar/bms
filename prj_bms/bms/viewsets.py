from django.shortcuts import render
from .models import Category, Brand, Shop, Invoice, Quantity, Shift
from rest_framework import viewsets, filters
from .serializers import CategorySerializer, BrandSerializer, ShopSerializer, InvoiceSerializer, QuantitySerializer, ShiftSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('category_id')
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_id', 'category_name', 'category_description')


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('brand_id', 'brand_name', 'brand_description')

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('shop_name', 'shop_owner', 'shop_address')

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('invoice_transaction_id',)

class QuantityViewSet(viewsets.ModelViewSet):
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('quantity_name', 'quantity_bottles')

class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('brand_id','stock_shift_date','stock_shift_from','stock_shift_to')
