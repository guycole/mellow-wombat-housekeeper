from django.urls import path

from . import views

app_name = "wombat"

urlpatterns = [
    path("", views.index, name="index"),
    path("heeler/", views.HeelerView.as_view(), name="heeler-list"),
]
