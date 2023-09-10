from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('applications.account.urls')),
    path('api/book_store/', include('applications.book_store.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
