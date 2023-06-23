from django.urls import path

from .views import (
    add_manager, get_manager, list_managers,
)

urlpatterns = [
    path("add/", add_manager),
    path("<int:pk>/", get_manager),
    path("all/", list_managers),
]

