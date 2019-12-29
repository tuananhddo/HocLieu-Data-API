from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    thumbnail_image = models.ImageField(upload_to='Image/books/',blank=True)

    def natural_key(self):
        return {'a':self.book_name,'b': str(self.thumbnail_image)}
class Unit(models.Model):
    unit_number = models.IntegerField()
    unit_name = models.CharField(max_length=100)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    # class Meta:
    #     unique_together = [['unit_number','book']]
    def natural_key(self):
        return  self.book.natural_key()

    natural_key.dependencies = ['API.Book']
class Word(models.Model):
    name = models.CharField(max_length=100)
    translated_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Image/words/',blank=True)
    sound = models.FileField(upload_to='Audio',blank=True)
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE)
class AppUser(models.Model):
    email = models.EmailField(max_length=120)
class LearnedWord(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
    word = models.ForeignKey(
        Word,
        on_delete=models.CASCADE,
    )
    listening = models.BooleanField()
    speaking = models.BooleanField()
    reading = models.BooleanField()
    writing = models.BooleanField()
