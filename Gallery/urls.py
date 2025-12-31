from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('upload/', views.upload_view, name='upload'),
    path('delete/<int:image_id>/', views.delete_image_view, name='delete_image'),
    path('edit/<int:image_id>/', views.edit_image_view, name='edit_image'),
]



