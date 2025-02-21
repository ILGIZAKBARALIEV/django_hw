from django.shortcuts import render
from . import models


# Create your views here.
def all_clothes(request):
    if request.method == "GET":
        all_clothes = models.Clothes.objects.all()
        return render(request, 'tags/all_clothes.html', context={'all_clothes': all_clothes})


def adult_clothes(request):
    if request.method == "GET":
        adult = models.Clothes.objects.filter(tags__title="Взрослая")
        return render(request, 'tags/adult_clothes.html', context={'adult': adult})


def teenager_clothes(request):
    if request.method == "GET":
        teenager = models.Clothes.objects.filter(tags__title="Подростковая")
        return render(request, 'tags/teenager_clothes.html', context={'teenager': teenager})


def kids_clothes(request):
    if request.method == "GET":
        kids = models.Clothes.objects.filter(tags__title="Детская")
        return render(request, 'tags/kids_clothes.html', context={'kids': kids})
