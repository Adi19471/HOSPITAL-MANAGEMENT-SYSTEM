from django.urls import path
from HospitalAPP import views
# import static files using dispaly all files store
from django.conf.urls.static import static
from django.conf import  settings


urlpatterns = [

       # login page
    path('',views.userlogin,name="userregistration"),
    path('login/',views.login_view,name="login"),
    path('logouts/',views.logout_view,name="logoutss"),


    path('home/',views.home_view,name="home"),
    # urls connct views to urls data... 4
    path('HospitalDepartment/',views.HospitalDepartment_view,name="HospitalDepartment"),
    # hospital_doctor_view...5 
    path('hospital-doctor/',views.hospital_doctor_view,name="hospital-doctor"),
    # hospital_patient_view....6
    path('hospital-patient-detailes/',views.hospital_patient_view,name="patient"),
    # CREATE TABLE hospital_roomKind..........-- 8
    path('hospital-room-kit/',views.hospital_roomKind_view,name='kit'),
    # CREATE TABLE hospital_room......................-- 9
    path('hospital-room/',views.hospital_room_view,name='room'),

  


    path('hospital-doctor-department/',views.hospital_doctor_departments_view,name="hospital-doctor-deepaartt"),


 

 
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)