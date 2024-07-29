from django.shortcuts import render

# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from api_app.models import Register,employee
from api_app.serializers import RegisterSerializer, LoginSerializer,employeeserializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from user.models import NewUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token



class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
   
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = serializer.get_tokens_for_user(user)
        
        return Response({
            'refresh': tokens['refresh'],
            'access': tokens['access']
        }, status=status.HTTP_200_OK)
        
class employeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    
    serializer_class = employeeserializer
    
    def list(self):
        payload = self.request.auth.payload
        jwt = JWTAuthentication()
        print('vansh')
        permission_classes = [IsAuthenticated]
        return self.queryset
    

# Create your views here.
