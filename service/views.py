from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewset(viewsets.ModelViewSet):
    """
    This viewset provides create, list, retrieve, update and delete actions.
    """

    queryset = Service.objects.all()
    serializer_class =  ServiceSerializer
