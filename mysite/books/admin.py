from django.contrib import admin
from .models import Book,Teacher,Editors


class ListingBook(admin.ModelAdmin):
    list_display =('id','Name','Author','Price')
    #list_display_links = ('id')
    #list_filter =('Name')
    #list_editable = ('Name')
    search_fields = ('id','Name','Author','Price')

class ListingTeacher(admin.ModelAdmin):
    list_display = ('id','Name','Age','City')
    search_fields=('id','Name','Age','City')

class ListingEditors(admin.ModelAdmin):
    list_display = ('id','Name','Age','City','Book_Name')
    search_fields=('id','Name','Age','City','Book_Name')


# Register your models here.
admin.site.register(Book,ListingBook)
admin.site.register(Teacher,ListingTeacher)
admin.site.register(Editors,ListingEditors)