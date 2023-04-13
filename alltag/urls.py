from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pages/", include("write_page.urls")),
    path("admin/", admin.site.urls),
    path("", include("head_page.urls")),
]
