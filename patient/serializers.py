from django.contrib.auth.models import User

from pydantic import ValidationError
from rest_framework import serializers
from . models import Patient


class PatientSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        # There will be two cases these are password mismatching & exists email
        if (password != confirm_password):
            raise serializers.ValidationError({'error': "Password Doestn't Matched"

                                               })
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "This email is already exist. Try with different one"

                                               })
        account = User(username=username, email=email, first_name=first_name,
                       last_name=last_name)
        account.set_password(password)
        account.is_active = False
        print(account)
        account.save()
        return account
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
  