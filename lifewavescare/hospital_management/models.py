from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=100, unique=True)
    patient_address = models.CharField(max_length=200, blank=True, null=True)
    patient_email = models.EmailField()
    patient_health_record = models.CharField(max_length=300)
    patient_mobile_number = models.CharField(max_length=16)


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100, unique=True)
    doctor_mobile_number = models.CharField(max_length=16)
    doctor_specialization = models.CharField(max_length=300)
    doctor_email = models.EmailField()

class Pharmacy(models.Model):
    pharmacy_id = models.AutoField(primary_key=True)
    pharmacy_email = models.EmailField()
    pharmacy_address = models.CharField(max_length=200)


class Appointment(models.Model):
    appoint_id = models.AutoField(primary_key=True)
    appoint_type = models.CharField(max_length=200)
