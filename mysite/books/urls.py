from django.conf.urls import url
from django.contrib import admin
from . import views

#We use this for namespace problem(namesapace proble, is that when we work on big project so many time
# diffrent file has same name from differnet app so it will not create any problem we use namespace)

app_name = 'books'

urlpatterns = [
    #/book
    url(r'^$',views.index,name="index"),
    #/book/2/
    url(r'^(?P<book_id>[0-9]+)/$',views.detail,name="detail"),
    url(r'^(?P<teacher_id>[0-9]+)/$',views.teacherDet,name="teacherDet")

    #url(r'^(?P<book_name>[\w\-]+)/$',views.byName,name="byName"),


]

