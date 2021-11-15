from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
# Create your models here.


# HOSPITAL DATA BASE 

# auth group ------------ 1
class auth_group(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)



    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.id

# create table auth_user ...........2
class auth_user(models.Model):
    id      	= models.IntegerField(primary_key=True)	
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    email  = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)

  

# CREATE TABLE auth_user_groups ...................-- 3

class auth_user_groups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(auth_user,on_delete=models.CASCADE)
    group_id = models.ForeignKey(auth_group,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

  


# CREATE TABLE hospital_department .....................4

class Hospital_department(models.Model):
    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)




# CREATE TABLE hospital_doctor ..........-- 5

class hospital_doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    user_id = models.ForeignKey(auth_user,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'hospital_doctor')
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)
  

# CREATE TABLE hospital_doctor_departments .........-- 6

class hospital_doctor_departments(models.Model):
    
    id = models.IntegerField(primary_key=True)
    doc_id = ForeignKey(hospital_doctor,on_delete=models.CASCADE)
    dep_id = ForeignKey(Hospital_department,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


# CREATE TABLE hospital_patient .........................-- 7

class hospital_patient(models.Model):

    id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=100)
    status   = models.BooleanField(default=True)
    user_id    = models.ForeignKey(auth_user,on_delete=models.CASCADE)
    admitDate = models.DateField(default=False)
    profile_pic =models.ImageField(upload_to = 'hospital_patient')
    assignedDoctorId   = models.ForeignKey(hospital_doctor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)



# CREATE TABLE hospital_roomKind..........-- 8
class hospital_roomKind(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)

# CREATE TABLE hospital_room......................-- 9

class hospital_room(models.Model):
    id = models.IntegerField(primary_key=True)
    roomNum = models.CharField(max_length=20)
    roomKindId = models.ForeignKey(hospital_roomKind,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)


# CREATE TABLE hospital_appointment ............-- 10

class hospital_appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    doctorId   = models.ForeignKey(hospital_doctor,on_delete=models.CASCADE)
    appointmentDate = models.DateField(auto_now=False)
    description     = models.TextField()
    status      = models.BooleanField(default=False)
    doctorName  = models.CharField(max_length=40)
    patientName  = models.CharField(max_length=40)
    patientId = models.ForeignKey(hospital_patient,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

# CREATE TABLE hospital_roombookings ............................-- 11

class hospital_roombookings(models.Model):
    id = models.IntegerField(primary_key=True)
    roomId = models.ForeignKey(hospital_room,on_delete=models.CASCADE)
    appointmentId   = models.ForeignKey(hospital_appointment,on_delete=models.CASCADE)
    startDatetime = models.DateTimeField(auto_created=False)
    endDatetime = models.DateTimeField(auto_created=False)

    def __str__(self):
        return str(self.id)


# CREATE TABLE hospital_patientInsurance ................-- 12
class hospital_patientInsurance(models.Model):
    id = models.IntegerField(primary_key=True)
    patientId   = models.ForeignKey(hospital_patient,on_delete=models.CASCADE)
    provider    = models.CharField(max_length=120)
    Insurance_Number    = models.CharField(max_length=120)
    Insurance_Type    = models.CharField(max_length=120)
    ExpiryDate      = models.DateField(auto_now=False)


    def __str__(self):
        return str(self.id)

# CREATE TABLE hospital_patientdischargedetails ...........-- 13

class hospital_patientdischargedetails(models.Model):
    id  = models.IntegerField(primary_key=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=100)
    admitDate   = models.DateField(auto_now=False)
    releaseDate   = models.DateField(auto_now=False)
    daySpent    = models.IntegerField(default=0)
    roomCharge  =models.DecimalField(max_digits=6, decimal_places=2)
    medicineCost = models.DecimalField(max_digits=6, decimal_places=2)
    doctorFee  = models.DecimalField(max_digits=6, decimal_places=2)
    OtherCharge  = models.DecimalField(max_digits=6, decimal_places=2)
    total   = models.DecimalField(max_digits=6, decimal_places=2)
    patientId  =  models.ForeignKey(hospital_patient,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

# CREATE TABLE Hospital_PaymentType...........-- 14

class Hospital_PaymentType(models.Model):

    id = models.IntegerField(primary_key=True)
    name    = models.CharField(max_length=150)


    def __str__(self):
        return str(self.id)

# CREATE TABLE Hospital_patientPayment............-- 15

class Hospital_patientPayment(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    paid   = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    paymentTypeId    = models.ForeignKey(Hospital_PaymentType,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    referenceDetails = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

# CREATE TABLE hospital_MedcineType ......-- 16
class hospital_MedcineType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)

# CREATE TABLE hospital_MedcineBrand ..........-- 17  
class hospital_MedcineBrand(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)



# CREATE TABLE hospital_Medcine ..........-- 18

class hospital_Medcine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    typeId = models.ForeignKey(hospital_MedcineType,on_delete=models.CASCADE)
    BrandId = models.ForeignKey(hospital_MedcineBrand,on_delete=models.CASCADE)
    UnitPrice   = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)

# CREATE TABLE hospital_dischargeMedication .......-- 19
class hospital_dischargeMedication(models.Model):
    id = models.IntegerField(primary_key=True)
    medcineID = models.ForeignKey(hospital_Medcine,on_delete=models.CASCADE)
    medcineName = models.CharField(max_length=150)
    dose = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.id)



# CREATE TABLE zipCode ......-- 20
class zipCode(models.Model):
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)

    def __str__(self):
        return str(self.id)
    

#   zip 	VARCHAR(10) 	NOT NULL,
#   city 	VARCHAR(90) 	NOT NULL,
#   state	VARCHAR(90) 	NOT NULL,
#   PRIMARY KEY (zip, city, state)
# );

# ALTER TABLE hospital_doctor ADD zipCode VARCHAR(10) NOT NULL,	ADD FOREIGN KEY (zipCode) REFERENCES zipCode (zip);
# ALTER TABLE hospital_patient ADD zipCode VARCHAR(10) NOT NULL, ADD FOREIGN KEY (zipCode) REFERENCES zipCode (zip);
