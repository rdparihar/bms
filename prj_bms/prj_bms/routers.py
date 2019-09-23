from rest_framework import routers
from bms.viewsets import CategoryViewSet, BrandViewSet, ShopViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'shop', ShopViewSet)

