#from django.http import HttpResponse
from .models import Book,Teacher,Editors
from django.shortcuts import render
from django.http import Http404

#render has inbuilt Httpresponse so insteed of passing request in hhtp directly pass in render

def index(request):
    all_books = Book.objects.all()
    all_teacher = Teacher.objects.all()
    all_editors = Editors.objects.all()
    context={
        'all_books': all_books,
        'all_teacher':all_teacher,
        'all_editors':all_editors
    }
    return render(request,'books/index.html',context)



def detail(request,book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("This Book Dose Not Exist")

    return render(request,'books/detail.html',{'book':book})
    #return HttpResponse("<h2>Details For Book Id:" +str(book_id)+ "</h2>")


def teacherDet(request,teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        raise Http404("Teacher Does Not Exist")

    return render(request,'books/teacherDet.html',{'teacher':teacher})

