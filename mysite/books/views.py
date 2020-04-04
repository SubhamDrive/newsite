from django.http import HttpResponse


# Create your views here.
#it will accept the request and send an http reponse.

def index(request):
    return HttpResponse("<h>This is the books homepage</h>")
