from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin
from django.views import generic
from .models import Category, Brand, Shop, Invoice, Quantity, Shift , BmsUser
from django.shortcuts import get_object_or_404

import datetime





class ShopListView(generic.ListView):
    context_object_name = 'shop_list'
    model = Shop
    queryset = Shop.objects.all()
    template_name = 'stocks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        userid = self.request.user.id
        context['user'] = self.request.user
        context['shop_list'] = self.model.objects.filter(shop_admin = userid)
        return context
 
     
class ShopDetailView( generic.DetailView):
    model = Shop
    template_name = "shop_details.html"
    
    def shop_detail_view(request, primary_key):
        shop = get_object_or_404(Shop, pk=primary_key)
        return render(request, context={'shop': shop})