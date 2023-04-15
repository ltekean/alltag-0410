from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path("logout/", views.logout, name="logout"),
    path("my-page/<int:user_id>/",views.my_page,name="my-page"),
    path("my-page/<int:user_id>/delete-image",views.profile_img_delete,name="profile_img_delete"),
    path("my-page/<int:user_id>/change-nickname",views.change_nickname,name="change_nickname")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# path('/post', views.profile_update, name='modify'),