from django.urls import path
from diary import views

urlpatterns = [
    path('', views.post, name='postHome'),
    path('home/', views.home, name='diaryHome'),
    path('create/', views.create, name="create"),
    path('diary_list/', views.diary_list, name="diary_list"),
]