from django.urls import path, include
from .views import SignupPageView


urlpatterns=[
    #ruta accounts/ es obligatorio tener ese nombre
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup", SignupPageView.as_view(), name= "signup"),
]