from django.urls import path
from django.contrib.auth import views as dj_view
from .views import RegistrationView, allStatment, CreateStatment, About, allService


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name='registration'),
    path("login/", dj_view.LoginView.as_view(), name='login'),
    path("logout/", dj_view.LogoutView.as_view(), name='logout'),
    path("", allStatment, name='allStatment'),
    path("createStatment/", CreateStatment, name='createStatment'),
    path("about/", About, name='about'),
    path("allService/", allService, name='allService')
]