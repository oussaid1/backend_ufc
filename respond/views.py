from django.shortcuts import render

from .serializers import UsersSerialiser
from .models import Users
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status,filters
# Create your views here.
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


def respond(request,board_id):
    data = User.objects.get(username = board_id)
    print(data.users.phone)
    return render(request,"responder/index.html",{'data':data})



# this is the view for the delete function
@api_view('DELETE')
#@permission_classes([IsAuthenticated,])
def delete(request,board_id):
    data = User.objects.get(username = board_id)
    data = data.Users
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# this is the view for the update function
@api_view('PUT')
def register(request,board_id):
        data = User.objects.get(username = board_id)
        data = data.Users
        ser = RegistrationSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

# this is the view for the signup
@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Token.objects.create(account)."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)



