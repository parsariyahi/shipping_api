from django.urls import path

from .views import (
    add_driver, get_driver, list_drivers,
    list_driver_carries,
)

urlpatterns = [
    path("add/", add_driver),
    path("<int:pk>/", get_driver),
    path("all/", list_drivers),
    path("<int:driver_id>/carries/all", list_driver_carries),
]
