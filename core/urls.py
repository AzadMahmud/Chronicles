from django.contrib import admin
from django.urls import include, path

from core import settings

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),
    path('api/blogs/', include('blogs.urls')),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)