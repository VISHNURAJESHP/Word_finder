from django.shortcuts import render
from .serializers import UserRegisterationSerializer, LoginSerializer
from .models import User
from rest_framework.response import Response
from django.conf import settings
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework.views import APIView

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
     
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        user = User.objects.filter(email=email).first()

        if User is None:
            raise AuthenticationFailed("Invalid email")

        if not User.check_password(password):

            raise AuthenticationFailed("invalid password")

        payload = {
            "id": User.id,
            "email": User.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }


        secret_key = settings.HASH_KEY 
        token = jwt.encode(payload, secret_key, algorithm="HS256")

        response = Response()
        response.set_cookie(
            key="jwt",
            value=token,
            httponly=False,
            samesite="None",
            secure=True,
            path="/",
        )
        response.data = {"jwt": token, "user": payload}
        return response