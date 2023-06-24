from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Carry
from .serializers import CarrySerializer

from user.models import CustomUser
from order.models import Order
from driver.models import Driver
from api.globals import token_finder, authenticate, get_user_obj, is_manager, is_driver, get_driver_location, distance


def nearest_driver(src_lat, src_long):
    drivers = Driver.objects.filter(is_free=True)
    driver_location_map = {}

    for driver in drivers:
        lat, long = get_driver_location(driver.id)
        driver_location_map[driver.id] = (lat, long)

    nearest = 0
    prev_dist = 0
    for driver, location in driver_location_map.items():
        dist = distance(src_lat, location[0], src_long, location[1])
        if not prev_dist:
            prev_dist = dist
        else:
            if dist < prev_dist:
                nearest = driver

    return nearest

@api_view(["POST"])
def add_carry(request):
    username = request.headers.get("UserName")

    user = get_user_obj(username=username)

    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if not is_manager(user):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    auth_token = request.headers.get("Authorization")
    token = token_finder(auth_token)

    if not authenticate(user, token):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    serializer = CarrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(["POST"])
def add_carry_auto(request):
    username = request.headers.get("UserName")

    user = get_user_obj(username=username)

    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if not is_manager(user):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    auth_token = request.headers.get("Authorization")
    token = token_finder(auth_token)

    if not authenticate(user, token):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    order = Order.objects.get(id=request.data["order"])
    request.data["driver"] = nearest_driver(order.src_lat, order.src_long)

    serializer = CarrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(["POST"])
def add_carry_manual(request):
    username = request.headers.get("UserName")

    user = get_user_obj(username=username)

    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if not is_manager(user):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    auth_token = request.headers.get("Authorization")
    token = token_finder(auth_token)

    if not authenticate(user, token):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    serializer = CarrySerializer(data=request.data)
    if serializer.is_valid():

        # check if the driver is free.
        driver_id = request.data.get("driver", None)
        driver = Driver.objects.get(pk=driver_id)
        if driver.is_free:
            driver.is_free = False
            driver.save()
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_carry(request, pk):
    username = request.headers.get("UserName")
    user = get_user_obj(username=username)
    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if not is_manager(user):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    auth_token = request.headers.get("Authorization")
    token = token_finder(auth_token)
    if not authenticate(user, token):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    carry = Carry.objects.get(pk=pk)
    serializer = CarrySerializer(carry)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_carries(request):
    username = request.headers.get("UserName")
    user = get_user_obj(username=username)
    if not user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if not is_manager(user):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    auth_token = request.headers.get("Authorization")
    token = token_finder(auth_token)
    if not authenticate(user, token):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    carries = Carry.objects.all()
    serializer = CarrySerializer(carries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def delivered_carry(request, pk):
    username = request.headers.get("UserName")
    user = get_user_obj(username=username)
    if not user:
        return Response("User Not Found", status=status.HTTP_401_UNAUTHORIZED)

    if not is_driver(user):
        return Response("User is Not Driver", status=status.HTTP_401_UNAUTHORIZED)

    auth_token = request.headers.get("Authorization")
    token = token_finder(auth_token)
    if not authenticate(user, token):
        return Response("Invalid Token", status=status.HTTP_401_UNAUTHORIZED)

    carry = Carry.objects.get(pk=pk)
    carry.delivered = True
    carry.delivered_at = datetime.now()
    carry.driver.is_free = True
    carry.driver.save()
    carry.save()

    return Response(status=status.HTTP_200_OK)