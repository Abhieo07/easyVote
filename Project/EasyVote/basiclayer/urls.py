from django.urls import path
from . import views

urlpatterns = [
    path('voting', views.voting, name="voting"),
    path('addface', views.addface, name="addface"),
]