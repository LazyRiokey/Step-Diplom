from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("workouts/", WorkoutsView.as_view(), name="workouts"),
    path("caregories/", CategoriesView.as_view(), name="categories"),
    path("caregories/<int:pk>/", CategoryDays.as_view(), name="basic"),
    path("caregories/<int:pk>/<int:day>/", DayListView.as_view(), name="day_workout"),
]