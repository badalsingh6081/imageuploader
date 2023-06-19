
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from myapp import views
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    
    path('acc/', include('sign.urls')),
    path('acc/', include('log.urls')),
    path('acc/', include('contact.urls')),
    path('acc/', include('core.urls')),
    path('acc/', include('change.urls')),
    path('acc/', include('reset.urls')),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

