from . import views
from django.urls import path

urlpatterns = [
    path("", views.see_main_page),
    path("<str:user_id>", views.see_detail_page),
]
