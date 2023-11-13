from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<str:user_url>/', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
