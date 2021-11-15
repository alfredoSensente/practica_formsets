"""library views"""
from django.shortcuts import get_object_or_404, render
from .models import Author, Book

# Create your views here.


def authors_list(request):
    """Show a book list"""
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'library/authors_list.html', context)

def add_books(request, id_author):
    """Add books to an author"""
    author = get_object_or_404(Author, pk = id_author)
    context = {
        'author': author,
    }
    return render(request, 'library/add_books.html', context)