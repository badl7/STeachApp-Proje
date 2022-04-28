from django.shortcuts import render


def ilanlar(request):
    return render(request,'pages/ilanlar.html')