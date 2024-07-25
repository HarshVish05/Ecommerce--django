from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Product

# serializers - wrap around certain model and turn them into json format
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # to return all the fields
        

class UserSerialzer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only = True)
    isAdmin = serializers.SerializerMethodField(read_only = True)
    _id = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'isAdmin'] 
    
    def get_isAdmin(self, obj):
        return obj.is_staff

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        name = f"{obj.first_name} {obj.last_name}"
        if name == "":
            name = obj.email
        return name
    

class UserSerialzerWithToken(UserSerialzer):
    token = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'name', 'isAdmin', 'token'] 
        
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)