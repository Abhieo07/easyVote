from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("index", views.index, name="index"),
    path("logout", views.logout, name="logout"),
    path("status", views.status, name="status"),#after signup we are rendering to the status page
    path("<str:part>", views.section, name="section"),
]