from django.db import models

# Create your models here.
# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    thumbnail_image = models.ImageField(upload_to='Image/books/',blank=True)
class Unit(models.Model):
    unit_number = models.IntegerField()
    unit_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
class Word(models.Model):
    name = models.CharField(max_length=100)
    translated_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Image/words/',blank=True)
    sound = models.FileField(upload_to='Audio',blank=True)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)