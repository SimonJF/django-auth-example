from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post_comment", views.post_comment),
    path("login", views.log_in),
    path("logout", views.log_out),
    path("register", views.register),
]
