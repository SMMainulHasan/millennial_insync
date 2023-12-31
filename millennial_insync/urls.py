from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('user/', include('user.urls')),
    path('article/', include('article.urls')),
]+ static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
