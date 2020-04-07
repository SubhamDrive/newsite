from django.db import models
from django.core.urlresolvers import reverse
class Book(models.Model):

    def get_absoulte_url(self):
        return  reverse('books.detail',kwargs={'pk:self.pf'})


    def __str__(self):
        return self.Name + "-"+ self.Author

    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)


class Teacher(models.Model):
    def __str__(self):
        return self.Name + "--" + self.Age

    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    City = models.CharField(max_length=50)


class Editors(models.Model):
    def __str__(self):
        return self.Name + "-" + self.Book_Name

    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=10)
    City = models.CharField(max_length=50)
    Book_Name = models.CharField(max_length=100)

"""
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    description = models.TextField(blank=True)
    phone  = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now(),blank=True)



    class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title   = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city    = models.CharField(max_length=100)
    state   = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price   = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    garage   = models.IntegerField(default=True)
    sqft    = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    last_date = models.DateTimeField(default=datetime.now(),blank=True)
    def __str__(self):
        return self.title

"""