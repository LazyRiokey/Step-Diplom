from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget

from .models import *

# Register your models here.


class WorkoutsAdminForm(forms.ModelForm):
    short_info = forms.CharField(widget=CKEditorWidget())
    full_info = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Workouts
        fields = "__all__"


class WorkoutsAdmin(admin.ModelAdmin):
    form = WorkoutsAdminForm
    list_display = [
        "id",
        "title",
        "workout_time",
        "short_info",
        "full_info",
        "image_data",
    ]
    list_editable = ["workout_time"]
    list_display_links = ["id", "title"]
    list_per_page = 10
    search_fields = ["title"]
    list_filter = ["title", "workout_time"]
    readonly_fields = ["image_data"]


admin.site.register(Workouts, WorkoutsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "short_description", "img", "image_data"]
    list_display_links = ["id", "title"]
    readonly_fields = ["image_data"]


admin.site.register(Categories, CategoriesAdmin)


class WorkoutsByDaysAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "day",
        "category_name",
        "time_coefficient",
        "get_workouts",
        "total_time",
        "is_completed",
    ]
    list_display_links = ["id", "day", "category_name"]
    list_editable = ["time_coefficient", "is_completed"]
    list_per_page = 10
    filter_horizontal = ["workouts"]
    search_fields = ["day", "get_workouts", "total_time"]
    list_filter = ["category_name", "is_completed"]


admin.site.register(WorkoutsByDays, WorkoutsByDaysAdmin)
