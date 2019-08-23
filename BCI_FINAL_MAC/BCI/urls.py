from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^', include('video.urls')),

    url(r'^video/', include('video.urls', namespace='vd')),

    url('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
