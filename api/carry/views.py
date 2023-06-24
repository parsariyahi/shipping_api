from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Carry
from .serializers import CarrySerializer

from user.models import CustomUser
from driver.models import Driver
from api.globals import token_finder, authenticate, get_user_obj, is_manager


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

    request.data["driver"] = Driver.objects.get(id=1)

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
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

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