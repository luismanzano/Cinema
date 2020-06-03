
from django.contrib import admin
from django.urls import path, include
from lairAdmin import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns







urlpatterns = [
    path('admin/', admin.site.urls),
    path('lairAdmin/', include('lairAdmin.urls')),
]

urlpatterns += staticfiles_urlpatterns()
