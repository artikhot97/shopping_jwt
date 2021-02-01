# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Chapter
from .serializers import ChapterSerializer
from rest_framework import filters
from product.serializers import DynamicSearchFilter #imported from product

#filter or search and add Chapter API
class ChapterAPIView(generics.ListCreateAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer