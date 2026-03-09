
from django.shortcuts import render,redirect
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes
# Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import smtplib

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UserLoginSerializer
from .models import Patient
from .serializers import PatientSerializer,RegistrationSerializer
from patient import serializers

class PatientViewset(viewsets.ModelViewSet):
    """
    This viewset provides create, list, retrieve, update and delete actions.
    """

    queryset = Patient.objects.all()
    serializer_class =PatientSerializer

class UserRegistrationApiview(APIView):
      serializer_class = RegistrationSerializer

      def post(self,request):
            serializer =  self.serializer_class(data=request.data)  
            if serializer.is_valid():
                try:
                    user = serializer.save()
                    token  = default_token_generator.make_token(user) # token generate korlam
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    # Build the confirm link dynamically using the request
                    scheme = request.scheme # usually http or https
                    host = request.get_host() # domain name
                    confirm_link = f"{scheme}://{host}/patient-api/active/{uid}/{token}/"
                    email_subject = "Confirm your Email"
                    email_body = render_to_string('confirm_mail.html',{'confirm_link':confirm_link})
                    email = EmailMultiAlternatives(
                        email_subject,
                        '',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[user.email],
                    )
                    email.attach_alternative(email_body, "text/html")
                    email.send()
                    return Response("Check your email")
                except Exception as e:
                    import traceback
                    traceback.print_exc() # Prints the actual error to your Render Logs
                    return Response({'error': f'User was saved, but something went wrong sending the email. Error: {str(e)}'}, status=400)
            return Response(serializer.errors)

def activate(request,uid64,token):
    try:
          uid = urlsafe_base64_decode(uid64).decode()
          user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
         user = None

    if user is not None and default_token_generator.check_token(user,token):
         user.is_active = True
         user.save()
         return redirect('login')
    else:
         return redirect('register')


class UserLoginApiView(APIView):
     def post(self, request):
          serializer = UserLoginSerializer(data=request.data)
          if serializer.is_valid():
               username = serializer.validated_data.get('username')
               password = serializer.validated_data.get('password')

               user = authenticate(username=username, password=password)
               if user:
                    token, _ = Token.objects.get_or_create(user=user)
                    login(request,user)
                    return Response({'token': token.key, 'user_id': user.id})
               return Response({'Error': 'Invalid Credentials'})
          return Response(serializer.errors)

               
      
    

class UserLogout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"success": "Successfully logged out"})