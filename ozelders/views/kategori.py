from django.shortcuts import render, get_object_or_404
from ozelders.models import IlanlarModel
from django.core.paginator import Paginator


def kategori(request, kategoriSlug):
    kategori = get_object_or_404
    print(kategoriSlug)
    ilanlar = IlanlarModel.objects.all()
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(ilanlar, 3)


    return render(request,'pages/ilanlar.html' , context= {
        'ilanlar': paginator.get_page(sayfa)
    })