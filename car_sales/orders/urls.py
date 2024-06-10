from django.urls import path
from .views import place_order, my_orders

urlpatterns = [
    path("place_order/<int:car_id>/", place_order, name="place_order"),
    path("my_orders/", my_orders, name="my_orders"),
]

