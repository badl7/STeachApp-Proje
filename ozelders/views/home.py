from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return HttpResponse("<h1>ANASAYFA</h1>")

