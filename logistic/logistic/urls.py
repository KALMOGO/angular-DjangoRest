
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("missions/", include('missions.urls')),
    path("maintenances/", include('maintenances.urls')),
    path("exercices/", include('exercices.urls')),
]
