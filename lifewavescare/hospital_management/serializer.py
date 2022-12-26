from . models import *

from rest_framework import serializers

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate(self,attrs):
        doctor_email = attrs.get("doctor_email", "")
        if doctor_email is None:
            raise serializers.ValidationError("Doctor_email field cannot be blank")

        doctor_mobile_number = attrs.get("doctor_mobile_number", "")
        if not doctor_mobile_number.startswith("9",3):
            raise serializers.ValidationError("mobile_number should be not correct")
        return super().validate(attrs)




class PatientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    def validate(self,attr):
        patient_email = attr.get("patient_email", "")
        if patient_email is None:
            raise serializers.ValidationError("Email cannot be blank")
        return super().validate(attr)


class PharmacyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'