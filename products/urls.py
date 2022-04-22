from django.urls import path
from . import views
from .views import ProductCreateView

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('home/', views.home),
    path('market/', views.market),
    path('about/', views.about),
    path('list/', ProductCreateView.as_view(), name='list')
]