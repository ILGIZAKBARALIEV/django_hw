from . import views
from django.urls import path

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('text_and_photo/', views.text_and_photo, name='text_and_photo'),
    path('time_now/', views.time_now, name='time_now'),

    path('books_list/', views.books_list, name='Books_list'),
    path('books/<int:id>/', views.books_detail_view, name='book_detail'),
]
