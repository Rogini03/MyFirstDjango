from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserRegister
from .serialization import UserRegisterSerializer


# Create your views here.
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getuser(request):
    user = UserRegister.objects.all()
    serial = UserRegisterSerializer(user, many=True)
    return Response(serial.data)

@api_view(['POST'])
def create(request):
    create= UserRegisterSerializer(data=request.data)
    if create.is_valid():
        create.save()
        return Response(create.data,status=status.HTTP_201_CREATED)
    else:
        return Response(create.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request,id):
    update=UserRegister.objects.get(id=id)
    upuser=UserRegisterSerializer(update,data=request.data)
    if upuser.is_valid():
        upuser.save()
        return Response(upuser.data,status=status.HTTP_200_OK)
    else:
        return Response(upuser.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete(request,id):
    deleteuser=UserRegister.objects.get(id=id)
    deleteuser.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


