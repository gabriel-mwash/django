from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

# Create your views here.


def book_list(request):
    """
    view  to display all books in the database
    """
    books = Book.objects.all() # fetch all book objects
    return render(request, "books/list.html", {"books": books})


def greeting(request):
    """
    greeting message to display
    """
    return HttpResponse("hello there django developer")
