from django.contrib import admin
from django.urls import path, inlcude

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
