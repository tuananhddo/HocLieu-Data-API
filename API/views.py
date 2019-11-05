from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from PIL import Image

size = 250, 250
# relative_path = "HocLieuAPI/"
relative_path = "API/"

def index(request,url_path):
    response = HttpResponse(content_type="image/png")
    img_path = relative_path + "Image/" + url_path
    try:
        img = Image.open(img_path)
        img.thumbnail(size)
        img.save(response, "JPEG")
    except IOError:
        return HttpResponse('This Image Not Exist')
    return response
def audio(request,audio_path):
    audio_path = relative_path + "Audio/" + audio_path
    try:
        f = open(audio_path, "rb")
        return HttpResponse(f,content_type="audio/mp3")
    except IOError:
        return HttpResponse('This Audio Not Exist')