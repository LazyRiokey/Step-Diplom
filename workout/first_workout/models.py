from django.utils.html import format_html
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.


class Workouts(models.Model):

    title = models.CharField(max_length=50)
    workout_time = models.PositiveIntegerField(
        validators=[MaxValueValidator(3600, "The value must not exceed 3600 seconds")]
    )
    short_info = models.TextField(max_length=400)
    full_info = models.TextField(max_length=1000)
    img = models.ImageField()

    def image_data(self):
        return format_html(
            '<img src="{}" width="150px"/>',
            self.img.url,
        )

    image_data.short_description = "Preview"

    def __str__(self):
        return self.title


class Categories(models.Model):

    title = models.CharField(max_length=20)
    short_description = models.TextField(max_length=50)
    img = models.ImageField()

    def image_data(self):
        return format_html(
            '<img src="{}" width="150px"/>',
            self.img.url,
        )

    image_data.short_description = "Preview"

    def __str__(self):
        return self.title


class WorkoutsByDays(models.Model):

    day = models.PositiveSmallIntegerField()
    category_name = models.ForeignKey(
        "Categories", verbose_name=("Category"), on_delete=models.PROTECT
    )
    workouts = models.ManyToManyField(Workouts)
    time_coefficient = models.FloatField()
    is_completed = models.BooleanField()

    def __str__(self):
        return f"{self.day} - {self.category_name}"

    def get_workouts(self):
        my_dict = {}
        for field in self.workouts.all():
            my_dict[field.title] = int(field.workout_time * self.time_coefficient)
        return my_dict

    get_workouts.short_description = "Workouts"

    def total_time(self):
        total_time = 0
        for field in self.workouts.all():
            total_time += field.workout_time * self.time_coefficient

        return f"{int(total_time / 60)} mins"
