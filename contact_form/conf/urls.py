from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('contacts.urls')),
    path('adminsite/', include('adminsite.urls')),
    path('admin/', admin.site.urls),
]