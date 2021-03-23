from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitquery', views.submitquery, name='submitquery'),
    path('suma/', views.suma, name='suma'),
    path('dinamico/', views.dinamico, name='dinamico'),
    path('multiple/', views.multiple, name='multiple'),
    #path('pruebaenvio', views.pruebaenvio, name='pruebaenvio'),
]