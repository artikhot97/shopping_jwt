# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
import json
# Create your views here.


class CartViewSet(generics.CreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class AddProdcutToCart(generics.APIView):
    def add(request):
        product = Product.objects.get(id=request.POST.get('product_id'))
        data = json.loads(request)
        Cart.objects.add(**data)
        return HttpResponse(1)

class RemoveCart(generics.APIView):
    def remove(request):
        cart = Cart(request.session)
        product = Product.objects.get(id=request.POST.get('product_id'))
        cart.remove(product)
        return HttpResponse()

