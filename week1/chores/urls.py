from django.urls import path
from . import views

app_name = "chores"

urlpatterns = [
    path("", views.chore_list, name="list"),
    path("create/", views.chore_create, name="create"),
    path("<int:pk>/toggle/", views.chore_toggle, name="toggle"),
]
