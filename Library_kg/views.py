from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models, forms
from django.views import generic
from django.urls import reverse


def about_me(request):
    return HttpResponse("Меня зовут Ильгиз ")


def text_and_photo(request):
    if request.method == 'GET':
        return  HttpResponse('<img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRLM_YMOn41npXKC5fX-TSRfe20jO-nK1cfON36eskj5100UzlH4JMmJVsjNYxZPV4R0vw6DHIw0dqN-osUB5Iw7Q" alt="cat gif" />Hello World')

def time_now(request):
    return  HttpResponse(f'Current time is: {datetime.now()}')

# create review

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book'

    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.CreateReviewForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('book_detail', kwargs={'id': self.object.choice_book.id})


# def create_review_view(request):
#     if request.method == "POST":
#         form = forms.CreateReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save(commit=False)
#             book_id = form.cleaned_data['choice_book'].id
#             form.save()
#             return redirect('book_detail', id=book_id)
#     else:
#         form = forms.CreateReviewForm()
#     return render(request, template_name='create_review.html', context={'form': form,})


class BookListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'books'
    model = models.BookModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


# def book_list_view(request):
#     if request.method == "GET":
#         query = models.BookModel.objects.all().order_by('-id')
#         context_object_name = {
#             'book': query,
#         }
#         return render(request, template_name='book.html', context=context_object_name)


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.BookModel, id=book_id)

# def book_detail_view(request, id):
#     if request.method == "GET":
#         query = get_object_or_404(models.BookModel, id=id)
#         context_object_name = {
#             'book_id': query,
#         }
#         return render(request, template_name='book_detail.html', context=context_object_name)

