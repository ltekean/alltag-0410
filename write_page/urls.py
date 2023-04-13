from . import views
from django.urls import path


urlpatterns = [
    path("write/", views.write_page_view, name="write"),
    path("", views.main, name="main"),
    path("main-page/", views.main_page_view, name="main"),
    path("create/", views.write_page_create, name="create"),
    # path("<str:user_id>", views.see_detail_page),
]
