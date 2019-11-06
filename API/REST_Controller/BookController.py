from django.http import HttpResponse
from django.core import serializers
from django.views import View
from API.models import Book
import json
class BookController(View):
    def get(self, request,id):
        return HttpResponse('Hello')
    def get(self, request):
        data = Book.objects.all().values()
        jsonData = json.dumps(list(data))
        return HttpResponse(jsonData, content_type='application/json')
