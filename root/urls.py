
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin2/', include("admin2.urls")),

    path('', include("apps.urls")),
]
