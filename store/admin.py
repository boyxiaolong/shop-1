from django.contrib import admin

# Register your models here.
from store import models
admin.site.register(models.Product)
admin.site.register(models.Address)
admin.site.register(models.Review)