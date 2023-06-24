from django.urls import path

from .views import (
    add_carry_manual, add_carry_auto, 
    get_carry, list_carries, delivered_carry
)

urlpatterns = [
    path("add/", add_carry_manual),
    path("add/auto", add_carry_auto),
    path("<int:pk>/", get_carry),
    path("<int:pk>/delivered", delivered_carry),
    path("all/", list_carries),
]