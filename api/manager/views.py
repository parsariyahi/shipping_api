from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Manager
from .serializers import ManagerSerializer

@api_view(["POST"])
def add_manager(request):
    serializer = ManagerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_manager(request, pk):
    try:
        driver = Manager.objects.get(pk=pk)
    except Manager.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serilizer = ManagerSerializer(driver)

    return Response(serilizer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_managers(request):
    managers = Manager.objects.all() 

    serilizer = ManagerSerializer(managers, many=True)

    return Response(serilizer.data)
