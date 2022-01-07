from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('create/', views.create, name='create'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/', views.update, name='update'),
    path('delete/<id>/', views.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Imagen
