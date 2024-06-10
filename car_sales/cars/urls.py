from django.urls import path
from .views import add_car, car_details

urlpatterns = [
    path("add/", add_car, name="add_car"),
    path("details/<int:id>/", car_details, name="car_details"),
]