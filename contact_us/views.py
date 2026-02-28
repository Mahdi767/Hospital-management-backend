from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Contactus
from .serializers import ContactUsSerializer

class ContactusViewset(viewsets.ModelViewSet):
    """
    This viewset provides create, list, retrieve, update and delete actions.
    """

    queryset = Contactus.objects.all()
    serializer_class = ContactUsSerializer
