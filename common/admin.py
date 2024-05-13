from django.contrib import admin
from common.models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    search_fields = ['file']
    list_filter = ['file_type']


@admin.register(CommonSettings)
class CommonSettingsAdmin(admin.ModelAdmin):
    list_filter = ['id', 'copyright']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ['id', 'text', 'author', 'stars']

