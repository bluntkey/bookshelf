from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q
from django.contrib.auth.decorators import login_required 

def index(request):
    query = request.GET.get('q')
    
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    else:
        books = Book.objects.all()
        
    return render(request, 'library/index.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def read_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/read_book.html', {'book': book})

from django.shortcuts import render, get_object_or_404, redirect # redirect


@login_required
def add_to_library(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    # Check if the user already has this book in their favorites
    if book.favorites.filter(id=request.user.id).exists():
        book.favorites.remove(request.user)
    else:
        book.favorites.add(request.user)
        
    # Go back to the book detail page
    return redirect('book_detail', book_id=book.id)

@login_required
def my_library(request):
    # Filter books where 'favorites' contains the logged-in user
    books = Book.objects.filter(favorites=request.user)
    return render(request, 'library/my_library.html', {'books': books})