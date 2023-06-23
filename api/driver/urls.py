from django.urls import path

from .views import (
    add_driver, get_driver, list_drivers,
)

urlpatterns = [
    path("add/", add_driver),
    path("<int:pk>/", get_driver),
    path("all/", list_drivers),
]
