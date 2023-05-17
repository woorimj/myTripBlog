from django.urls import path
from info import views

urlpatterns = [
    path('', views.home, name='infoHome')
]