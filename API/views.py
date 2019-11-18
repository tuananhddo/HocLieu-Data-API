import json
import os

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from PIL import Image

from API.models import Book, Unit, Word

size = 250, 250
# relative_path = "HocLieuAPI/"
relative_path = "API/"

def image(request,url_path):
    response = HttpResponse(content_type="image/png")
    try:
        img = Image.open(url_path)
        img.thumbnail(size)
        img.save(response, "JPEG")
    except IOError:
        return HttpResponse('This Image Not Exist')
    return response
def audio(request,audio_path):
    # audio_paths = relative_path + "Audio/sample.mp3"
    try:
        f = open(audio_path, "rb")
        return HttpResponse(f,content_type="audio/mp3")
    except IOError:
        return HttpResponse('This Audio Not Exist')
def getUnitByBook(request,bookId):
    data = Unit.objects.filter(book_id=bookId).values('id','unit_number','unit_name')
    jsonData = json.dumps(list(data))
    return HttpResponse(jsonData, content_type='application/json')
def getWordByUnit(request,unitId):
    data = Word.objects.filter(unit_id=unitId).values('id','name','translated_name','description','image','sound')
    jsonData = json.dumps(list(data))
    return HttpResponse(jsonData, content_type='application/json')


def getBookById(request):
    data = Book.objects.filter(id=2).values()
    jsonData = json.dumps(list(data)[0])
    return HttpResponse(jsonData, content_type='application/json')
