from unicodedata import name
from django.urls import path,include
from ozelders.models import kategori
from ozelders.views import iletisim
from ozelders.views import ilanlar, kategori, ilanlarim
from ozelders.views.home import homePage
from account.views import profil






urlpatterns = [
    path('', homePage,name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('profil', profil, name='profil'),
    path('ilanlar', ilanlar, name='ilanlar'),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('ilanlarim', ilanlarim, name='ilanlarim'),
]

