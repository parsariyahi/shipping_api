from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from driver.models import Driver
from driver.serializers import DriverSerializer

@api_view(["POST"])
def add_driver(request):
    serializer = DriverSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(status=status.HTTP_201_CREATED)


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