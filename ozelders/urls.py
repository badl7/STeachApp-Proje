from unicodedata import name
from django.urls import path,include
from ozelders.models import kategori
from ozelders.views import iletisim
from ozelders.views import profil
from ozelders.views.home import homePage







urlpatterns = [
    path('', homePage,name='anasayfa'),
    path('iletisim', iletisim, name='iletisim'),
    path('profil', profil, name='profil'),
]
