from django.urls import path
from . import views

urlpatterns = [
    path("", views.Page, name="page"),
    # path('', views.is_liked_view.view),
    # path('main/', views.main, name=="main_page")
]
