from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.BookModel)
class BookModel(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'price', 'email', 'created_at']
    list_filter = ['genre', 'created_at']
    search_fields = ['title', 'author', 'genre']


@admin.register(models.Review)
class Review(admin.ModelAdmin):
    list_display = ['book', 'stars', 'created_at']
    list_filter = ['stars', 'created_at']
    search_fields = ['book']