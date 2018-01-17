# -*- coding: utf-8 -*-
# czat/urls.py

from django.conf.urls import url
from . import views  # import widoków aplikacji
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from czat.models import Wiadomosc
from django.views.generic import DeleteView

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rejestracja/', CreateView.as_view(template_name='czat/rejestracja.html', form_class=UserCreationForm , success_url=reverse_lazy('czat:index'))),
    url(r'^logowanie/', auth_views.login, {'template_name': 'czat/logowanie.html'}, name='logowanie'),
    url(r'^wylogowanie/', auth_views.logout, {'next_page' : reverse_lazy('czat:index')}, name='wylogowanie' ),
    url(r'^wiadomosci/', login_required(ListView.as_view(model=Wiadomosc, context_object_name='wiadomosci', paginate_by=5)), name='wiadomosci'),
    url(r'^dodaj/$', login_required(views.DodajWiadomosc.as_view(),login_url='/logowanie'), name='dodaj'),
    url(r'^edytuj/(?P<pk>\d+)/', login_required( views.EdytujWiadomosc.as_view(), login_url='/logowanie'), name='edytuj'),
    url(r'^usun/(?P<pk>\d+)/', login_required( DeleteView.as_view(model=Wiadomosc, template_name='czat/wiadomosc_usun.html', success_url = '/wiadomosci'), login_url='/logowanie'), name='usun'),

]
