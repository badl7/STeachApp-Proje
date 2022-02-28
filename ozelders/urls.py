from django.urls import path

from ozelders.views import homePage



urlpatterns = [
    path('', homePage),
]
