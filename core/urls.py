from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from article.views import home__page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home__page),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
