from django.shortcuts import render
from django.views import generic

from django.shortcuts import HttpResponse

from .models import MainGenre, SubGenre, Game

def index(request):
    return HttpResponse("Hello, world. This is the database index page.")
