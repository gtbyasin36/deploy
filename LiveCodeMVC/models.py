from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
# Create your models here.

class CategoryId(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class ProductMobil(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=3000)
    images = models.ImageField(upload_to='')
    category_id = models.ForeignKey(CategoryId, default='',  on_delete=models.CASCADE,)
    location = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductMotor(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=3000)
    images = models.ImageField(upload_to='')
    category_id = models.ForeignKey(CategoryId, default='', on_delete=models.CASCADE)
    location = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductElectronics(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=3000)
    images = models.ImageField(upload_to='')
    category_id = models.ForeignKey(CategoryId, default='',  on_delete=models.CASCADE)
    location = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)