from rest_framework import viewsets
from rest_framework import filters
from . models import Doctor,Designation,Specialization,AvailableTime,Review
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import DoctorSerializer,ReviewSerializer,AvailableTimeSerializer,DesignationSerializer,SpecializationSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

class DoctorPagination(PageNumberPagination):
    page_size = 1 # 1 item per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class =ReviewSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class =DesignationSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class =SpecializationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = AvailableTime.objects.all()
    serializer_class =AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]
