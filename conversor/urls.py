from django.urls import path
from .views import salvar_video,download

urlpatterns = [
    path('', salvar_video, name='home'),
    path('download', download, name='download'),
]