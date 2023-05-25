from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from diary import views

urlpatterns = [
    path('', views.post, name='postHome'),
    path('home/', views.home, name='diaryHome'),
    path('create/', views.diary_create, name="create"),
    path('diary_list/', views.diary_list, name="diary_list"),
    path('diary_detail/<int:id>/', views.diary_detail, name='diary_detail'),
    path('diary_update/<int:id>/', views.diary_update, name='diary_update'),
    path('diary_delete/<int:id>/', views.diary_delete, name='diary_delete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)