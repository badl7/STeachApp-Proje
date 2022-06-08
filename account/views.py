from django.shortcuts import render

# Create your views here.



def profil(request):
    return render(request,'pages/profil.html')



def ilanlarim(request):
    return render(request, 'pages/ilanlarim.html')