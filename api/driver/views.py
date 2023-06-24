from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Driver
from .serializers import DriverSerializer

from carry.models import Carry
from carry.serializers import CarrySerializer
from user.serializers import UserSerializer

@api_view(["POST"])
def add_driver(request):
    request.data["role"] = 2
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_driver(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serilizer = DriverSerializer(driver)

    return Response(serilizer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def list_drivers(request):
    drivers = Driver.objects.all() 

    serilizer = DriverSerializer(drivers, many=True)

    return Response(serilizer.data)

@api_view(["GET"])
def list_driver_carries(request, driver_id):
    carries = Carry.objects.filter(driver=driver_id)
    serializer = CarrySerializer(carries, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
