from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('download/<file>/<filename>', download_file, name="download"),
]