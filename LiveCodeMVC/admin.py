from django.contrib import admin
from .models import ProductMobil, ProductMotor, ProductElectronics, CategoryId

# Register your models here.
admin.site.register(ProductMobil)
admin.site.register(ProductMotor)
admin.site.register(ProductElectronics)
admin.site.register(CategoryId)