from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from .models import Car
from .forms import CommentForm
from django.db import IntegrityError

def add_car(request):
    return render(request, "add_car.html")

def car_details(request, id):
    car = Car.objects.get(pk=id)
    comments = car.comments.filter(car=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                form.instance.car = car
                form.save()
                return redirect(reverse_lazy("car_details", kwargs={"id": id}))
            except IntegrityError:
                form.add_error('email', 'This email has already been used to comment on this car.')
    else:
        form = CommentForm()
    return render(request, "car_details.html", {"car": car, "comment_form": form, "comments": comments})

