from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from conversor import urls as conv_urls

urlpatterns = [
    path('', include(conv_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
