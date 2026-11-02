from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-django-project-trooth/', admin.site.urls),
    path('admin/', include('Trooth_Forum_App.urls')),
    path('', include('Trooth_Forum_App.urls'))
]
