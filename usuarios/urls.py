
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('cadastrar_avaliador/',views.cadastrar_avaliador,name='cadastrar_avaliador'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
]