from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from PIL import Image

size = 250, 250

def index(request,url_path):
    response = HttpResponse(content_type="image/png")
    img_path = "HocLieuAPI/Image/" + url_path
    try:
        img = Image.open(img_path)
        img.thumbnail(size)
        img.save(response, "JPEG")
    except IOError:
        return HttpResponse('This Image Not Exist')
    return response
