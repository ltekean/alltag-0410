from . import views
from django.urls import path

urlpatterns = [
    path("write/", views.write_page_view, name="write"),
    path("", views.main, name="main"),
    path("main-page/", views.main_page_view, name="main-page"),
    path("main-page/<int:writes_id>/", views.detail_page_view, name="detail-writes"),
    path("create/", views.write_page_create, name="create"),
    path("main-page/<int:writes_id>/edit/", views.write_page_edit, name="edit"),
    path("main-page/<int:writes_id>/delete/", views.write_page_delete, name="delete"),
    # path("<str:user_id>", views.see_detail_page),
]
