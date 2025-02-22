from . import views
from django.urls import path

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('text_and_photo/', views.text_and_photo, name='text_and_photo'),
    path('time_now/', views.time_now, name='time_now'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('create_review/<int:book_id>/', views.CreateReviewView.as_view(), name='create_review'),

]

