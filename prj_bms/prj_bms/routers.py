from rest_framework import routers
from bms.viewsets import CategoryViewSet, BrandViewSet, ShopViewSet, InvoiceViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'shop', ShopViewSet)
router.register(r'invoice', InvoiceViewSet)

