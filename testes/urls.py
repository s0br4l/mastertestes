from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medidas', views.medidas, name='medidas'),
    path('testes', views.testes, name='testes'),
    path('lista', views.lista, name='lista'),
    ]

