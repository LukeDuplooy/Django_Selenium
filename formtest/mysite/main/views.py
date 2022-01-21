from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car

# Create your views here.
def homepage(request):
  if request.method == "POST":
    form = CarForm(request.POST)
    if form.is_valid():
        form.save()
  cars = Car.objects.all()
  form = CarForm()
  return render(request, "home.html", {"form": form, "cars": cars})



