from django.shortcuts import render
from ozelders.models import IlanlarModel
from django.core.paginator import Paginator


def ilanlar(request):
    ilanlar = IlanlarModel.objects.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(ilanlar, 3)


    return render(request,'pages/ilanlar.html' , context= {
        'ilanlar': paginator.get_page(sayfa)
    })