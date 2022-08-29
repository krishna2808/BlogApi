
from rest_framework import serializers
from api.models import User 
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from api.utils import Util


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', ]
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise  serializers.ValidationError("Password is not match")
        return attrs 
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)  

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']
        # extra_kwargs = {
        #     'password' : {'write_only': True}
        # }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']

class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password1 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    
    
    class Meta:
        fields = ['password', 'password1']
    def validate(self, attrs):
        user = self.context.get('user')
        password = attrs.get('password')
        password1 = attrs.get('password1')
        print('***********', password, password1)
        if password != password1:
            raise serializers.ValidationError('Password is not match ')
        user.set_password(password)
        user.save()
        return attrs 

class sendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user_id = user.id 
            print("user id", user_id)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("encoded uid ", uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token :', token)
            link = 'http://localhost:8000/api/user/reset/' + uid + '/'+token 
            print('Password rest link ', link)
            body = 'Click Following link to Reset Your password ' + link
            # send email
            # data = {
            #     'subject' : 'Reset Your Password', 
            #     'body' : body,
            #     'to_email' : user.email, 
                
            # }

            # Util.send_email(data)

            return attrs 
        else:
            raise serializers.ValidationError('You are not a Registered User')

class UserResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password1 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    
    
    class Meta:
        fields = ['password', 'password1']
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password1 = attrs.get('password1')
            uid = self.context.get('uid')
            token = self.context.get('token')

            print('***********', password, password1)
            if password != password1:
                raise serializers.ValidationError('Password is not match ')   
            id  = smart_str(urlsafe_base64_decode(uid))  
            print("decode uid  but it is byte format :", urlsafe_base64_decode(uid), '\nuid converted to smart_str : ', id )
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError('Token is not valid or Expired ')
            user.set_password(password)
            user.save()
            return attrs     

        except DjangoUnicodeDecodeError as error:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not valid or Expired ')




        

        user.set_password(password)
        user.save()
        return attrs 




          



