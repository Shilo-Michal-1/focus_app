from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('current/', views.current, name='current'),
    path('expenses/', views.expanses, name='expanses'),
]
