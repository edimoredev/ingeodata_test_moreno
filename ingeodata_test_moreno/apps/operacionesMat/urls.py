from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('adjuntarFile/', adjuntarFile, name='adjuntarFile'),
    path('fileDelete/<str:file>', fileDelete, name='fileDelete'),
]
