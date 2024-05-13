from django.contrib import admin
from mix.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Mix)
class MixAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'strength']
    list_filter = ['category']
    search_fields = ['title']


@admin.register(MixTag)
class MixTagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(MixComponent)
class MixComponentAdmin(admin.ModelAdmin):
    list_display = ['title']