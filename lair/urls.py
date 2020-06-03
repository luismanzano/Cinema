
from django.contrib import admin
from django.urls import path, include
from lairAdmin import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('lairAdmin/', include('lairAdmin.urls')),
]

#Con esto anexamos a las rutas el uso de los archivos estaticos como nuestos css
urlpatterns += staticfiles_urlpatterns()
#Con esto anexamos el uso de archivos multimedia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
