from django.contrib import admin
from lounge.models import *


@admin.register(Metro)
class MetroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Lounge)
class LoungeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'location']
    search_fields = ['title']


@admin.register(LoungeImage)
class LoungeAdmin(admin.ModelAdmin):
    list_display = ['id', 'lounge']
    search_fields = ['lounge']