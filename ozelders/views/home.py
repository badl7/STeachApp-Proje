from django.shortcuts import render
from ozelders.models import kategori


def homePage(request): 
    return render(request,'pages/anasayfa.html')




