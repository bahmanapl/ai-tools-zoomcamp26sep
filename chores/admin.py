from django.contrib import admin
from .models import Household, Roommate, Chore


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "created_at")
    search_fields = ("name",)


@admin.register(Roommate)
class RoommateAdmin(admin.ModelAdmin):
    list_display = ("name", "household")
    list_filter = ("household",)
    search_fields = ("name",)


@admin.register(Chore)
class ChoreAdmin(admin.ModelAdmin):
    list_display = ("title", "household", "assigned_to", "status", "created_at")
    list_filter = ("status", "household")
    search_fields = ("title",)
