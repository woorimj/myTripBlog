from django.urls import path, include
from info import views

urlpatterns = [
    path('', views.home, name='infoHome'),
    path('accounts/', include('accounts.urls')),
]