from rest_framework import serializers
from . models import Doctor,Designation,Specialization,AvailableTime,Review
from patient.models import Patient

class DoctorSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # designation = serializers.StringRelatedField(many=True)
    # specialization = serializers.StringRelatedField(many=True)
    # available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = Doctor
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    # reviewer = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    # doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())

    class Meta:
        model = Review
        fields = '__all__'
        

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'
        
class  DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'

class   AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'
