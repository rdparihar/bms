from django.urls import path, include
from django.views.generic import TemplateView
# urls of the app_users
urlpatterns = [
    # path('', views.IndexView.as_view()),
    path('', TemplateView.as_view(template_name='shops.html'), name="home"),
    path('category/', TemplateView.as_view(template_name='category.html'), name="category"),
    path('brand/', TemplateView.as_view(template_name='brand.html'), name="brand"),
    # path('brand/(?<id>.+)/$', TemplateView.as_view(template_name='brand.html'), name="brand"),

    path('shop/', TemplateView.as_view(template_name='shop.html'), name="shop"),
    path('invoice/', TemplateView.as_view(template_name='invoices.html'), name="invoice"),
    path('quantity/', TemplateView.as_view(template_name='quantities.html'), name="quantity"),
    path('shift/', TemplateView.as_view(template_name='shifts.html'), name="shift"),

    
]