import json
import os

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.core.serializers import json as jsx

# Create your views here.
from django.http import HttpResponse, Http404
# from PIL import Image
import Image
from API.models import Book, Unit, Word,LearnedWord,AppUser

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


def getWordById(request,wordId):
    data = Word.objects.filter(id=wordId).values()
    jsonData = json.dumps(list(data)[0])
    return HttpResponse(jsonData, content_type='application/json')
def getUserInfoByEmail(request,email):
    data = AppUser.objects.filter(email = email).values();
    if data.exists():
        jsonData = json.dumps(list(data)[0])
        return HttpResponse(jsonData, content_type='application/json')
    raise Http404("No Data matches the given query.")

#TODO:Secure Undone POST
def create_or_update_user(request,email):
    if AppUser.objects.filter(email=email).exists():    #Update
        data = AppUser.objects.all().values();
        jsonData = json.dumps(list(data))
        return HttpResponse(jsonData, content_type='application/json')
    else:   #Create
        newUser = AppUser(email = email)
        newUser.save()
        data = AppUser.objects.all().values();
        jsonData = json.dumps(list(data))
        return HttpResponse(jsonData, content_type='application/json')
def getLearnedWordByUser(request,email):
    try:
        user = AppUser.objects.get(email = email)
        data = LearnedWord.objects.filter(user=user)
        jsonData = json.dumps(list(data))
        return HttpResponse(jsonData, content_type='application/json')
    except ObjectDoesNotExist:
        print("Either the entry or blog doesn't exist.")
        raise Http404("No Data matches the given query.")


def getBookById(request):
    data = Book.objects.filter(id=2).values()
    jsonData = json.dumps(list(data)[0])
    return HttpResponse(jsonData, content_type='application/json')