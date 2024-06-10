from django.shortcuts import render

def add_brand(request):
    return render(request, "add_brand.html")
