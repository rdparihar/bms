from django.shortcuts import render
from .models import Category, Brand, Shop, Invoice, Quantity, Shift , BmsUser
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, BrandSerializer, ShopSerializer, InvoiceSerializer, QuantitySerializer, ShiftSerializer
from .serializers import BmsUserSerializer , UserSerializer
from .serializers import ReadCategorySerializer, ReadBrandSerializer, ReadShopSerializer, ReadInvoiceSerializer, ReadQuantitySerializer, ReadShiftSerializer
from .serializers import ReadBmsUserSerializer , ReadUserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings



class CategoryViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Category.objects.all().order_by('category_id')
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadCategorySerializer
        elif self.request.method == 'POST':
            return CategorySerializer
        else:
            return ReadCategorySerializer
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_id', 'category_name', 'category_description')


class BrandViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Brand.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadBrandSerializer
        elif self.request.method == 'POST':
            return BrandSerializer
        else:
            return ReadBrandSerializer
    serializer_class = BrandSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['category_id__category_id',]

class UserViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadUserSerializer
        elif self.request.method == 'POST':
            return UserSerializer
        else:
            return ReadUserSerializer
    serializer_class = UserSerializer
   
class BmsUserViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = BmsUser.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadBmsUserSerializer
        elif self.request.method == 'POST':
            return BmsUserSerializer
        else:
            return ReadBmsUserSerializer
    serializer_class = BmsUserSerializer

class ShopViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Shop.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadShopSerializer
        elif self.request.method == 'POST':
            return ShopSerializer
        else:
            return ReadShopSerializer
    serializer_class = ShopSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('shop_name', 'shop_owner', 'shop_address', 'shop_admin')

class QuantityViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Quantity.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadQuantitySerializer
        elif self.request.method == 'POST':
            return QuantitySerializer
        else:
            return ReadQuantitySerializer
    serializer_class = QuantitySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('quantity_name', 'quantity_bottles')

class ShiftViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Shift.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadShiftSerializer
        elif self.request.method == 'POST':
            return ShiftSerializer
        else:
            return ReadShiftSerializer
    serializer_class = ShiftSerializer 
    filter_backends = (filters.SearchFilter,)
    search_fields = ('brand_id','stock_shift_date','stock_shift_from','stock_shift_to')

class InvoiceViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Invoice.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadInvoiceSerializer
        elif self.request.method == 'POST':
            return InvoiceSerializer
        else:
            return ReadInvoiceSerializer
    serializer_class = InvoiceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_id')