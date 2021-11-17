from django.urls import path
from HospitalAPP import views
# import static files using dispaly all files store
from django.conf.urls.static import static
from django.conf import  settings


urlpatterns = [

       # login page
    path('',views.user_signup,name="userregistration"),
    path('login/',views.user_login,name="login"),
    path('logouts/',views.user_logout,name="logoutss"),




    path('home/',views.home_view,name="home"),
    # urls connct views to urls data... 4
    path('HospitalDepartment/',views.HospitalDepartment_view,name="HospitalDepartment"),
    # hospital_doctor_view...5 
    path('hospital-doctordata/',views.hospital_doctor_view,name="hospital-doctor"),
    # hospital_patient_view....7
    path('hospital-patient-detailes/',views.hospital_patient_view,name="patient"),
    # CREATE TABLE hospital_roomKind..........-- 8
    path('hospital-room-kit/',views.hospital_roomKind_view,name='kit'),
    # CREATE TABLE hospital_room......................-- 9
    path('hospital-room/',views.hospital_room_view,name='room'),
    # CREATE TABLE hospital_appointment ............-- 10
    path('hospital-appointment/',views.hospital_appointment_view,name='appointment'),
    # CREATE TABLE hospital_roombookings ............................-- 11
    path('hospital-roombooking/',views.hospital_roombookings_view,name='roombooking'),
    # CREATE TABLE hospital_patientInsurance ................-- 12
    path('hospital-patient-insurence/',views.hospital_patientInsurance_view,name='patientInsurence'),
    # CREATE TABLE hospital_patientdischargedetails ...........-- 13
    path('hospital-patient-discharge-detailes/',views.hospital_patientdischargedetails_view,name='patientdischarge'),
    # CREATE TABLE Hospital_PaymentType...........-- 14
    path('hospital-ppayment-type/',views.Hospital_PaymentType_view,name='payment'),
    # CREATE TABLE Hospital_patientPayment............-- 15
    path('hospital-paient-payment/',views.Hospital_patientPayment_view,name='patientpayment'),
    # CREATE TABLE hospital_MedcineType ......-- 16
    path('hospital-medicine-type/',views.hospital_MedcineType_view,name='medicine'),
    # CREATE TABLE hospital_MedcineBrand ..........-- 17  
    path('hospital-medicine-brand/',views.hospital_MedcineBrand_view,name='medicine-brand'),

    # CREATE TABLE hospital_Medcine ..........-- 18
    path('hospital-medicine/',views.hospital_Medcine_view,name='hospital-medicine'),
    # CREATE TABLE hospital_dischargeMedication .......-- 19
    path('hospital-hospital_discharge-Medication/',views.hospital_dischargeMedication_view,name='discharge-medicine'),
    # CREATE TABLE zipCode ......-- 20
    path('zipCode/',views.zipCode_view,name='zipcode'),



    path('hospital-doctor-department/',views.hospital_doctor_departments_view,name="hospital-doctor-deepaartt"),


 

 
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)