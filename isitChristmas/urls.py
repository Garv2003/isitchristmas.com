# urls.py
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("", include("hello.urls")),
    path("static/", include("django.contrib.staticfiles.urls")),
]