from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from . import models, forms
from django.shortcuts import redirect

def about_me(request):
    return HttpResponse("Меня зовут Ильгиз ")


def text_and_photo(request):
    if request.method == 'GET':
        return  HttpResponse('<img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLM_YMOn41npXKC5fX-TSRfe20jO-nK1cfON36eskj5100UzlH4JMmJVsjNYxZPV4R0vw6DHIw0dqN-osUB5Iw7Q" alt="cat gif" />Hello World')

def time_now(request):
    return  HttpResponse(f'Current time is: {datetime.now()}')


def books_list(request):
    if request.method == 'GET':
        books = models.BookModel.objects.all()
        return render(request, 'book.html', {'books': books})

def books_detail_view(request, id):
    if request.method == 'GET':
        book = models.BookModel.objects.get(id=id)
        form = forms.ReviewForm()
        context_object_name = {
            'book':book,
            'form':form
        }
        book = models.BookModel.objects.get(id=id)
        return render(request, 'book_detail.html', context=context_object_name)
    elif request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            book = models.BookModel.objects.get(id=id)
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('books_detail_view', id=id)
        else:
            return HttpResponse('Form is not valid')