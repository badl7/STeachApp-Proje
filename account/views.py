from django.shortcuts import render, get_object_or_404
from ozelders.models import IlanlarModel, KategoriModel
from django.core.paginator import Paginator

"""
def ilanlarım(request, kategoriSlug):
    
    ilanlar = kategori.ilan.order_by('-id')
    
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(ilanlar, 3)


    return render(request,'pages/kategori.html' , context= {
        'ilanlar': paginator.get_page(sayfa),
        'kategori_ders': kategori.ders,
    })

"""
def profil(request):
    return render(request,'pages/profil.html')



