from django.shortcuts import render, redirect
from cars.models import Car
from .models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request, car_id):
    car = Car.objects.get(pk=car_id)
    if car.quantity == 0:
        messages.warning(request, "Sorry, we don't have enough quantity in stock.")
    else:
        order = Order(
            user=request.user,
            car=car,
            quantity=1,
            price=car.price
        )
        order.save()
        car.quantity -= 1
        car.save()
        messages.success(request, "Your order has been placed successfully.")
    
    return redirect("home")

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "my_orders.html", {"orders": orders})