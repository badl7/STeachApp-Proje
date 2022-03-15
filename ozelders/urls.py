from django.urls import path,include
from ozelders.views import iletisim
from ozelders.views import profil
from ozelders.views.home import homePage







urlpatterns = [
    path('home', homePage),
    path('iletisim', iletisim),
    path('profil', profil),
]
