from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('',include('entudio.urls')),
]

admin.site.site_header = "Entudio Admin"
admin.site.site_title = "Entudio"
