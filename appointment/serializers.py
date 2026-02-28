from rest_framework import serializers
from . models import Appointment
from patient.models import Patient
from doctor.models import Doctor
class AppointmentSerializer(serializers.ModelSerializer):
    # patient =serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    # doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    

    class Meta:
        model = Appointment
        fields = '__all__'
        

    