from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='home'),
    path('create/', views.create, name='create'),
    path('post_list/', views.post_list, name='post_list'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    path('update/<int:id>/', views.post_update, name='post_update'), 
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
