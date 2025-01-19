from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.base, name='base'),
    path("signup/", views.signup, name='signup'),
    path("signin/", views.signin, name='signin'),
    path("signout/", views.signout, name='signout'),
    path("profile/", views.profile, name='profile'),
]