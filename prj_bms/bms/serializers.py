from .models import Category, Brand
from .models import Shop
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ['category_id','category_name','category_description']


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields =  '__all__'

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields =  '__all__'