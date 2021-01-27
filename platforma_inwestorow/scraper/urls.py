from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mailing_assign', views.mailing_assign, name='mailing_assign')
]
