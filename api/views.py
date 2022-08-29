

from rest_framework import status
from api.serializers import UserLoginSerializer, UserRegistrationSerializer, \
    UserProfileSerializer, UserChangePasswordSerializer, sendPasswordResetEmailSerializer, \
    UserResetPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
       
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()   
            token = get_tokens_for_user(user)         
            return Response({'msg': 'Created account', 'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.
         HTTP_400_BAD_REQUEST)


class UserloginView(APIView):
    def get(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            # print('**********', email, password)
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'msg': 'Login account', 'token': token}, status=status.HTTP_200_OK)
            else: 
 
             return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
        return Response(serializer.errors, status=status.
         HTTP_400_BAD_REQUEST)

        

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        # if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        print(request.user)
        
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            print(serializer.data)
            return Response({'msg': 'Change password '},  status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SendPasswordResetEmailView(APIView):
    def post(self, request,format=None):
        serializer = sendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': 'Password Reset link send. please check you email'},status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPasswordResetView(APIView):
    def post(self, request, uid, token, format=None):
        serializer = UserResetPasswordSerializer(data=request.data, context={'uid':uid, 'token':token}) 
        if serializer.is_valid():
            return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
         







