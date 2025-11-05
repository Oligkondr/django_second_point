from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import books
from books.forms import BookForm
from books.models import Book


# Create your views here.
def test(request: WSGIRequest):
    return render(request, 'test.html')

@method_decorator(csrf_exempt, name='dispatch')
class BooksView(View):
    model = Book

    def get(self, request, book_id=None):
        if book_id is None:
            books = Book.objects.all()
            return render(request, 'books_list.html', {'books': books})
        try:
            book = Book.objects.get(id=book_id)
            form = BookForm(instance=book)
            return render(request, 'book_info.html', {'book': book, 'form': form})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def post(self, request, book_id=None):
        # Проверка на “фейковый DELETE”
        if book_id and request.POST.get('_method') == 'DELETE':
            book = get_object_or_404(Book, id=book_id)
            book.delete()
            return redirect('books_list')

        # обычная обработка редактирования
        if book_id is None:
            return JsonResponse({'error': 'Book ID is required for update'}, status=400)
        book = get_object_or_404(Book, id=book_id)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book', book_id=book.id)
        return render(request, 'book_info.html', {'book': book, 'form': form})

    # def delete(self, request, book_id):
    #     book = get_object_or_404(Book, id=book_id)
    #     book.delete()
    #     return JsonResponse({'message': 'Book deleted successfully'})

@method_decorator(csrf_exempt, name='dispatch')
class BookCreateView(View):
    template = 'book_form.html'

    def get(self, request):
        form = BookForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('book', book_id=book.id)
        return render(request, self.template, {'form': form})
