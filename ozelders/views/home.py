from django.shortcuts import render


def homePage(request):
    context = {
        "isim" : "Betül Gürbüz"
    }
    return render(request,'pages/anasayfa.html', context={})

