from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('blog/', include('blog.urls')),
    path('charts/', include('charts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('indicators/', include('indicators.urls')),
    path('news/', include('news.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
