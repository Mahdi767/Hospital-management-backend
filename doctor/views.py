from rest_framework import viewsets
from . models import Doctor,Designation,Specialization,AvailableTime,Review
from .serializers import DoctorSerializer,ReviewSerializer,AvailableTimeSerializer,DesignationSerializer,SpecializationSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class =ReviewSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class =DesignationSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class =SpecializationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class =AvailableTimeSerializer
