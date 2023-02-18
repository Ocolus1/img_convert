from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("download/<file>/<filename>", download_file, name="download"),
    path("register", register, name="register"),
    path("login_user", login_user, name="login_user"),
    path("logout_user", logout_user, name="logout_user"),
    path("privacy_policy", privacy_policy, name="privacy_policy"),
    path("terms_and_condition", terms_cond, name="terms_and_condition"),
    path("cookie_policy", cookie_policy, name="cookie_policy"),
]