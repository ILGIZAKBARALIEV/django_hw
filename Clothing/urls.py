from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes, name='all_clothes'),
    path('teenager_clothes/', views.teenager_clothes, name='teenager_clothes'),
    path('kids_clothes/', views.kids_clothes, name='kids_clothes'),
    path('adult_clothes/', views.adult_clothes, name='adult_clothes'),
]
