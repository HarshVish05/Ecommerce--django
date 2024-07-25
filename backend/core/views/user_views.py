from django.shortcuts import render

# rest_framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

# rest_framework - simpleJWT auth
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import Product, User
from core.serializers import UserSerialzer, UserSerialzerWithToken

# for hashing the password
from django.contrib.auth.hashers import make_password

# for customizing tokens 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # values to be returned without decoding
        # data['username'] = self.user.username
        # data['email'] = self.user.email
    
        # above code can be written as this cause we have created UserSerialzerWithToken
        serializer = UserSerialzerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data
    
    
    
    # one way of customizing the message we get from tokens after decoding
    
    # @classmethod
    # def get_token(cls, user):
    #     token = super().get_token(user)

    #     # Add custom claims
    #     token['username'] = user.username
    #     token['message'] = "custom message for understanding"
    #     # ...

    #     return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    
@api_view(['POST'])
def register_user(request):
    data = request.data
    # print(request.data)
    try:
        user = User.objects.create(
            first_name = data['first_name'],
            last_name = data['last_name'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password']),
        )
        
        serializer = UserSerialzerWithToken(user, many = False)

        return Response(serializer.data)
    
    except:
        message = {'message': 'User with this email already exists'}
        return Response(message, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])      # will only allow the permitted user
def getUserProfile(request):
    user = request.user  # we cant use this method here cause of the decorator it excepts us to provide the info via tokens
    serializer = UserSerialzer(user, many = False)

    return  Response(serializer.data)

@api_view(['GET']) 
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerialzer(users, many = True) 
    return Response(serializer.data)

