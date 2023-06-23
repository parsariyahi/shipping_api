from django.urls import path

from .views import (
    add_order, get_order, list_orders,
)

urlpatterns = [
    path("add/", add_order),
    path("<int:pk>/", get_order),
    path("all/", list_orders),
]


