from django.contrib import admin
from tobacco.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Taste)
class TasteAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'manufacturer', 'country']
    search_fields = ['title', 'tag']
    list_filter = ['country', 'taste', 'type', 'manufacturer']


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PrepMethod)
class PrepMethodAdmin(admin.ModelAdmin):
    list_display = ['title']
