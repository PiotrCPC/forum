from django.urls import path
from . import views




urlpatterns = [
    path('', views.base, name='base'),
    path('wyniki', views.wyniki, name='wyniki'),
    path('tresc', views.tresc, name='tresc'),
    path('o_nas', views.o_nas, name='o_nas'),
    path('dodaj_wpis', views.dodaj_wpis, name='dodaj_wpis'),
    path('twojeimie', views.twojeimie, name='twojeimie'),
    path('drugi', views.drugaopcja, name='drugaopcja'),
    
    path('persony', views.person_view, name='person_view'),
    path('formularz', views.formularz, name='formularz'),

]
