from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('articles/', include('articles.urls')),
  path('admin/', admin.site.urls),
  path('about/', views.about),
  path('', views.home),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)