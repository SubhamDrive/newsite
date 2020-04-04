from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    #/book
    url(r'^$',views.index,name="index"),
    #/book/2/
    url(r'^(?P<book_id>[0-9]+)/$',views.detail,name="detail"),
    url(r'^(?P<book_name>[\w\-]+)/$',views.byName,name="byName"),


]

