from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewset(viewsets.ModelViewSet):
    """
    This viewset provides create, list, retrieve, update and delete actions.
 """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
#custom query korlam
    def get_queryset(self):
        queryset = super().get_queryset() #13 no line ke niye ashlam
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)

        return queryset
           
    def get_queryset(self):
        queryset = super().get_queryset() #13 no line ke niye ashlam
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)

        return queryset
           
        
