from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(auth_group)
class auth_groupAdmin(admin.ModelAdmin):
    list_dispaly = ['id','name']
admin.site.register(auth_user)
admin.site.register(auth_user_groups)
admin.site.register(Hospital_department)
admin.site.register(hospital_doctor)
admin.site.register(hospital_doctor_departments)
admin.site.register(hospital_patient)
admin.site.register(hospital_roomKind)
admin.site.register(hospital_room)
admin.site.register(hospital_appointment)
admin.site.register(hospital_roombookings)
admin.site.register(hospital_patientInsurance)
admin.site.register(hospital_patientdischargedetails)
admin.site.register(Hospital_PaymentType)
admin.site.register(Hospital_patientPayment)
admin.site.register(hospital_MedcineType)
admin.site.register(hospital_MedcineBrand)
admin.site.register(hospital_Medcine)
admin.site.register(hospital_dischargeMedication)
admin.site.register(zipCode)

