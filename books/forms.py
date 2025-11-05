from django import forms

from authors.models import Author
from books.models import Book, Genre


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=False,
        empty_label="Select author"
    )

    co_authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'publication_year', 'genres', 'co_authors', 'summary']
        widgets = {
            'title': forms.TextInput(),
            'isbn': forms.TextInput(),
            'publication_year': forms.DateInput(),
            'summary': forms.Textarea(),
        }
