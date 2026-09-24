from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("inscription/", views.register_view, name="register"),
    path("connexion/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("deconnexion/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("cours/", views.courses, name="courses"),
    path("annonces/", views.announcements, name="announcements"),
    path("emploi-du-temps/", views.schedule, name="schedule"),
]
