from django.urls import path
from . import views
from .views import add, defaultPath

urlpatterns= [
    path('', views.defaultPath, name='defaultPath'),
    path('add/', views.add, name='add')
]