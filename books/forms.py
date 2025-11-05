from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_year', 'genres', 'co_authors', 'summary']
        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput(),
            'isbn': forms.NumberInput(),
            'publication_year': forms.DateInput(),
            'genres': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'co_authors': forms.TextInput(),
            'summary': forms.Textarea(),
        }
