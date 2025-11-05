from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods

import books
from books.forms import BookForm
from books.models import Book


# Create your views here.
def test(request: WSGIRequest):
    return render(request, 'test.html')


class BooksView(View):
    model = Book
    template_name = 'book_list.html'

    def get(self, request):
        all_books = Book.objects.all()

        return render(request, self.template_name, {'books': all_books})

    # def post(self, request):

@require_http_methods(['GET', 'POST'])
def create(request: WSGIRequest):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponse('saved')
    else:
        form = BookForm()
        return render(request, 'book_form.html', {'form': form})
