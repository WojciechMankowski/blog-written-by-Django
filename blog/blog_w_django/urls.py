from django.contrib import admin
from django.urls import path, include
from wpisy import urls

urlpatterns = [path("admin/", admin.site.urls), path("", include(urls))]
