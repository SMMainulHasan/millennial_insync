from django.urls import path

from user.views import user_login, user_logout, user_registration

urlpatterns = [
    path("register/", user_registration, name ='register'),
    path("login/", user_login, name ="login"),
    path("logout/", user_logout, name ='logout'),
]
