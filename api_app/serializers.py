# api/serializers.py

from rest_framework import serializers
from user.models import NewUser
from rest_framework_simplejwt.tokens import RefreshToken
from api_app.models import Register
from django.contrib.auth import authenticate
from api_app.models import employee
from rest_framework_simplejwt.authentication import JWTAuthentication

# serializer for the register API
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = NewUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid login credentials")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'")
        
        data['user'] = user
        return data

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model =  employee
        fields = '__all__'        