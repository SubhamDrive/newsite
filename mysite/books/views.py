from django.http import HttpResponse
from .models import Book
from django.shortcuts import render
from django.http import Http404

#render has inbuilt Httpresponse so insteed of passing request in hhtp directly pass in render
def index(request):
    all_books = Book.objects.all()
    context={
        'all_books': all_books
    }
    return render(request,'books/index.html',context)

def detail(request,book_id):
    try:
        book = Book.object.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("This Book Dose Not Exist")

    context={
        'book':book
    }

    return render(request,'books/detail.html',book)
    #return HttpResponse("<h2>Details For Book Id:" +str(book_id)+ "</h2>")

def byName(request,book_name):
    return HttpResponse("<h2>Details For Book_name: " +str(book_name)+ "</h2>")