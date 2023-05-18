from django.contrib import admin
from django.urls import path, include
from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),
    path('create/', views.create, name='create'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    path('update/<int:id>/', views.post_update, name='post_update'), 
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
]