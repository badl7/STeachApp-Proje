from django.shortcuts import render
from ozelders.models import kategori

def profil(request):
    return render(request,'pages/profil.html')
