from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('diary/', include('diary.urls')),
    path('info/', include('info.urls')),
    path('contact/', include('contact.urls')),
]