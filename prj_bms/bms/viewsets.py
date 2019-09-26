from django.shortcuts import render
from .models import Category, Brand, Shop, Invoice, Quantity, Shift , BmsUser
from django.contrib.auth.models import User
from rest_framework import viewsets, filters
# from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, BrandSerializer, ShopSerializer, InvoiceSerializer, QuantitySerializer, ShiftSerializer
from .serializers import BmsUserSerializer , UserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings


class CategoryViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Category.objects.all().order_by('category_id')
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_id', 'category_name', 'category_description')


class BrandViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('brand_id',)
    search_fields = ['category_id__category_id',]

class UserViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = User.objects.all()
    serializer_class = UserSerializer
   
class BmsUserViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = BmsUser.objects.all()
    serializer_class = BmsUserSerializer

class ShopViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('shop_name', 'shop_owner', 'shop_address', 'shop_admin')

class InvoiceViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (filters.SearchFilter,)
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('category_id')
    search_fields = ('category_id')

class QuantityViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Quantity.objects.all()
    serializer_class = QuantitySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('quantity_name', 'quantity_bottles')

class ShiftViewSet(LoginRequiredMixin,viewsets.ModelViewSet):
    login_url = settings.LOGIN_REDIRECT_URL
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('brand_id','stock_shift_date','stock_shift_from','stock_shift_to')

