from django.db import models

class Book(models.Model):

    def __str__(self):
        return self.Name + "-"+ self.Author

    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

