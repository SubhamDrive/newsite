from django.http import HttpResponse
from .models import Book
# Create your views here.
#it will accept the request and send an http reponse.

def index(request):
    all_books = Book.objects.all()
    html=''
    for book in all_books:
        url = '/books/' + str(book.id) + "/"
        html+= '<a href="'+ url +'">' + str(book.Name) + '</a><br>'
    return HttpResponse(html)


def detail(request,book_id):
    return HttpResponse("<h2>Details For Book Id:" +str(book_id)+ "</h2>")

def byName(request,book_name):
    return HttpResponse("<h2>Details For Book_name: " +str(book_name)+ "</h2>")