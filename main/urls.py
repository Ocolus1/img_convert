from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('download/<file>/<filename>', download_file, name="download"),
    path("register", register, name="register"),
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
    path('', include('social_django.urls', namespace='social'))
]