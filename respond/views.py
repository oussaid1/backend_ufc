from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .serializers import UsersSerialiser,RegistrationSerializer,LoginSerializer
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
    return render(request,"responder/index.html",{'data':data})



# # this is the view for the delete function
# @api_view('DELETE')
# #@permission_classes([IsAuthenticated,])
# def delete(request,board_id):
#     # data = User.objects.get(username = board_id)
#     # data = data.Users
#     # data.delete()
#     return Response(request=status.HTTP_204_NO_CONTENT)

# this is the view for the update function
@api_view(['GET', 'PUT', 'DELETE'])
def register(request,board_id):
        data = User.objects.get(username = board_id)
        data = data.Users
        ser = RegistrationSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

# this is the view for the signup
@api_view(['GET', 'PUT', 'DELETE'])
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

# this is the view for the signup
 
@api_view(['POST', ])
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            username = serializer.data.get('username')
            data = User.objects.get(email=serializer.data['email'])
            username =data.username
            user = authenticate(username=username, password=serializer.data['password'])
        if user == None:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        else:
            token = Token.objects.get(user_id= data.id).key
            print(token)
            return Response(token,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def get_social_profiles_view(request):
    data=[]
    data.append[{
        "name":"Twitter",
        "url":"https://twitter.com/",
        "icon":"twitter"
        },
        {
        "name":"Facebook",
        "url":"https://facebook.com/",
        "icon":"facebook"
        },
        {
        "name":"Instagram",
        "url":"https://instagram.com/",
        "icon":"instagram"
        },
        {
        "name":"LinkedIn",
        "url":"https://linkedin.com/",
        "icon":"linkedin"
        },
        {
        "name":"Github",
        "url":"https://github.com/",
        "icon":"github"
        }

        ]

    return Response(data)

