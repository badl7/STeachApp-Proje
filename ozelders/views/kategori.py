from django.shortcuts import render, get_object_or_404
from ozelders.models import IlanlarModel, KategoriModel
from django.core.paginator import Paginator


def kategori(request, kategoriSlug):
    kategori = get_object_or_404(KategoriModel, slug=kategoriSlug)
    ilanlar = kategori.ilan.order_by('-id')
    print(ilanlar)
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(ilanlar, 3)


    return render(request,'pages/ilanlar.html' , context= {
        'ilanlar': paginator.get_page(sayfa)
    })