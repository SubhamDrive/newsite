from django.http import HttpResponse
from .models import Book
from django.shortcuts import render

#render has inbuilt Httpresponse so insteed of passing request in hhtp directly pass in render
def index(request):
    all_books = Book.objects.all()
    context={
        'all_books': all_books
    }
    return render(request,'books/index.html',context)

def detail(request,book_id):
    return HttpResponse("<h2>Details For Book Id:" +str(book_id)+ "</h2>")

def byName(request,book_name):
    return HttpResponse("<h2>Details For Book_name: " +str(book_name)+ "</h2>")