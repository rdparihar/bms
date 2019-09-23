from django.urls import path, include
from django.views.generic import TemplateView
# urls of the app_users
urlpatterns = [
    # path('', views.IndexView.as_view()),
    path('category/', TemplateView.as_view(template_name='category.html')),
    path('brand/', TemplateView.as_view(template_name='brand.html')),
    path('shop/', TemplateView.as_view(template_name='shop.html')),
    
]