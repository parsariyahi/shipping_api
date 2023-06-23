from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Order
from .serializers import OrderSerializer

from user.models import CustomUser
from api.globals import token_finder, authenticate, get_user_obj, is_manager

@api_view(["POST"])
def add_order(request):
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

    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(["GET"])
def get_order(request, pk):
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

    order = Order.objects.get(pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def list_orders(request):
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

    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)