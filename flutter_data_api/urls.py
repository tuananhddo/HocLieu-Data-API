"""flutter_data_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from API import views
from API.REST_Controller.BookController import BookController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('image/<path:url_path>', views.image),
    path('audio/<path:audio_path>', views.audio),
    path('book/',BookController.as_view()),
    path('unit/<int:bookId>',views.getUnitByBook),
    path('word/<int:unitId>', views.getWordByUnit),

    path('word/id/<int:wordId>', views.getWordById),

    path('user/info/<str:email>',views.getUserInfoByEmail),
    path('user/<str:email>',views.create_user),
    path('user/learned/update',views.update_learner_word),

    # path('user/learned',views.getLearnedWordByUser),
    path('user/learned/<str:email>',views.getLearnedWordByUser),
    #Test
    path('book/id', views.getBookById),

]
