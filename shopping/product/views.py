# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from product.models import User
from product.serializers import UserSerializer,ProductsSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from product.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import filters


#Register and get list of all user 
class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserManager.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['chapter_name','author','concept__concept_text']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

#Dynamic Filter 
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


# Product View
class ProductsViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    filter_backends = (DynamicSearchFilter,)
    queryset = Products.objects.all().order_by('-name')
    serializer_class = ProductsSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Create your views here.
class PaginationView(GenericAPIView):
    """
    This API for Pagination View for Order List for easy to get no of data length 
    """
    serializer_class = ProductsSerializer
    queryset = User.objects.all()  # query set data
    pagination_class = CustomPagination

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data  # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '200',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)