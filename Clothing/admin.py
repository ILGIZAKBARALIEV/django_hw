from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('tags',)
    search_fields = ('title', 'tags__title')
