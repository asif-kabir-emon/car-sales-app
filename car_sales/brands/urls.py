from django.urls import path
from .views import add_brand

urlpatterns = [
    path("add/", add_brand, name="add_brand"),
]
