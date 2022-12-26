from django.contrib import admin
from django.urls import path
from . views import PatientListView, DoctorListView, PharmacyListView, AppointmentListView, DoctorDetailView, \
    PatientDetailView,PharmacyDetailView, AppointmentDetailView

urlpatterns = [
    path('patientlist', PatientListView.as_view(), name='PatientListView'),
    path('doctorlist', DoctorListView.as_view(), name='DoctorListView'),
    path('pharmacylist', PharmacyListView.as_view(), name='PharmacyListView'),
    path('appointmentlist', AppointmentListView.as_view(), name='AppointmentListView'),
    path('doctordetail/<pk>', DoctorDetailView.as_view(), name='DoctorDetailView'),
    path('patientdetail/<pk>', PatientDetailView.as_view(), name='PatientDetailView'),
    path('pharmacydetail/<pk>', PharmacyDetailView.as_view(), name='PharmacyDetailView'),
    path('appointmentdetail/<pk>', AppointmentDetailView.as_view(), name='AppointmentDetailView')
]
