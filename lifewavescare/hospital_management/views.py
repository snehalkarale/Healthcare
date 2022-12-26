from django.shortcuts import render
from rest_framework import request, status
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from . models import *
from . serializer import DoctorListSerializer, PatientListSerializer, PharmacyListSerializer, AppointmentListSerializer

class DoctorListView(APIView):
    def get(self,request):
        count = Doctor.objects.all()
        serializer = DoctorListSerializer(count, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = DoctorListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetailView(APIView):
    def get(self,request,pk):
        result = Doctor.objects.get(pk=pk)
        serializer = DoctorListSerializer(result)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        result = Doctor.objects.get(pk=pk)
        serializer = DoctorListSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        result = Doctor.objects.get(pk=pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PatientListView(APIView):
    def get(self,request):
        count = Patient.objects.all()
        serializer = PatientListSerializer(count, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = PatientListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetailView(APIView):
    def get(self,request,pk):
        result = Patient.objects.get(pk=pk)
        serializer = PatientListSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        result = Patient.objects.get(pk=pk)
        serializer = PatientListSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        result = Patient.objects.get(pk=pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PharmacyListView(APIView):
    def get(self,request):
        count = Pharmacy.objects.all()
        serializer = PharmacyListSerializer(count, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = PharmacyListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PharmacyDetailView(APIView):
    def get(self,request,pk):
        result = Pharmacy.objects.get(pk=pk)
        serializer = PharmacyListSerializer(result)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        result = Pharmacy.objects.get(pk=pk)
        serializer = PharmacyListSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        result = Pharmacy.objects.get(pk=pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppointmentListView(APIView):
    def get(self,request):
        count = Appointment.objects.all()
        serializer = AppointmentListSerializer(count, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetailView(APIView):
    def get(self,request,pk):
        result = Appointment.objects.get(pk=pk)
        serializer = AppointmentListSerializer(result)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        result = Appointment.objects.get(pk=pk)
        serializer = AppointmentListSerializer(result,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        result = Appointment.objects.get(pk=pk)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)