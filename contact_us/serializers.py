from rest_framework import serializers
from . models import Contactus
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contactus
        fields = '__all__'
        