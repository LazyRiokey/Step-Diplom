from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import UserLoginForm, UserRegisterForm, WorkoutsByDaysForm
from .models import *

# Create your views here.


def index(request):
    return render(request, "first_workout/index.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Registration error..")
    else:
        form = UserRegisterForm()
    return render(request, "first_workout/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "first_workout/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


class CategoryDays(ListView):
    model = WorkoutsByDays
    template_name = "first_workout/category_days.html"
    # allow_empty = False

    def get_queryset(self):
        return WorkoutsByDays.objects.filter(category_name_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = Categories.objects.get(id=self.kwargs["pk"])
        return context


class DayListView(ListView):
    model = WorkoutsByDays
    template_name = "first_workout/cur_day.html"

    def post(self, request, *args, **kwargs):
        cat = Categories.objects.get(pk=self.kwargs["pk"])
        obj = WorkoutsByDays.objects.get(day=self.kwargs["day"])
        obj.is_completed = True
        obj.save()
        return redirect("basic", cat.pk)

    def get_queryset(self):
        return WorkoutsByDays.objects.filter(pk=self.kwargs["day"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["day"] = WorkoutsByDays.objects.get(day=self.kwargs["day"])
        return context


class WorkoutsView(ListView):
    model = Workouts
    template_name = "first_workout/workouts.html"
    paginate_by = 12


class CategoriesView(ListView):
    model = Categories
    template_name = "first_workout/categories.html"
