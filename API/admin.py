from django.contrib import admin

# Register your models here.
from API.models import Word,Unit,Book

admin.site.register(Word)
admin.site.register(Unit)
admin.site.register(Book)

