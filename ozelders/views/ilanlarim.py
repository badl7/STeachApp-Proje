from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def ilanlarim(request):
    
    ilanlarim = request.user.ilanlar.order_by('-id')
    sayfa = request.GET.get('sayfa')
    paginator = Paginator(ilanlarim, 3)


    return render(request,'pages/ilanlarim.html' , context= {
        'ilanlarim': paginator.get_page(sayfa),
        
    })