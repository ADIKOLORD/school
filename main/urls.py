from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static

from school.views import AdministrationAPIViewSet
from .yasg import urlpatterns as doc_urls
from . import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('administration', AdministrationAPIViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('school.urls')),
    path('', include(router.urls)),
] 

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)