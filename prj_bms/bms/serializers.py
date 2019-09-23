from .models import Category, Brand
from .models import Shop
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = ['category_id','category_name','category_description']


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    brand_id = serializers.ReadOnlyField()
    category_id = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Category.objects.all())
    class Meta:
        model = Brand
        fields =  ['brand_id','brand_name','brand_description','category_id','brand_p_cost','brand_q_cost','brand_n_cost','brand_d_cost','brand_l_cost','brand_xg_cost','brand_y_cost','brand_p_sale','brand_q_sale','brand_n_sale','brand_d_sale','brand_l_sale','brand_xg_sale','brand_y_sale']

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    shop_id = serializers.ReadOnlyField()
    class Meta:
        model = Shop
        fields =   ['shop_id','shop_name', 'shop_owner', 'shop_address']
