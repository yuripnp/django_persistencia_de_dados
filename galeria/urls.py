from django.urls import path
from .views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<str:foto_id>', imagem, name='imagem'),
]