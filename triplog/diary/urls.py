from django.urls import path
from diary import views

urlpatterns = [
    path('', views.post, name='postHome'),
    path('home/', views.home, name='diaryHome'),
]