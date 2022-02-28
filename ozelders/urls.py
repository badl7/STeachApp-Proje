from django.urls import path

from ozelders.views import homePage, iletisim



urlpatterns = [
    path('', homePage),
    path('iletisim', iletisim),
]
