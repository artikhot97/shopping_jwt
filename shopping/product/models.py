# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class User(AbstractUser):
    username = models.CharField(blank=True, null=True,max_length=20)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password','first_name','last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

class Category(models.Model):
    category_type = models.CharField(max_length=50)
    class Meta:
        db_table = 'category'

class Brand(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        db_table = 'brand'

class Products(models.Model):
    category = models.ForeignKey(Category, related_name='category')
    brand = models.ForeignKey(Brand, related_name='brand')
    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    rating = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(default='Product description.')


    def get_price(self, request):
        return self.price

    def get_qut_price(self, request):
        return self.quantity * self.price

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'products'