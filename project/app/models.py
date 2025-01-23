from django.db import models

class Adhare(models.Model):
    adhare_no=models.IntegerField(unique=True)
    created_by=models.CharField(max_length=50)
    created_date=models.DateField()
    def __str__(self):
        return str(self.adhare_no)
    # def __str__(self):
    #     return self.created_by

class UserProfile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    Contect=models.IntegerField()
    adhar_no=models.OneToOneField(Adhare,on_delete=models.PROTECT)
    def __str__(self):
        return self.name

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return str(self.dep_name)
    dep_description=models.CharField(max_length=50)
    dep_Hod=models.CharField(max_length=50)

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_father_name=models.CharField(max_length=50)
    stu_DateOfBirth=models.DateField()
    stu_Email=models.EmailField()
    stu_department=models.ForeignKey(Department,on_delete=models.PROTECT, to_field='dep_name')
    stu_RollNumber=models.CharField(max_length=20, unique=True)  
    def __str__(self):
        return self.stu_name 
    
class Vehicle(models.Model):
    vename=[('Tata','Tata'),('BMW','BMW'),('Audi','Audi'),('Hyundai','Hyundai'),('Hounda','Hounda')]
    ve_name=models.CharField(max_length=50, choices=vename)
    veriant_type=[('Tata','Altra'),('BMW','BMW X1'),('Audi','Audi Q5'),('Hyundai','verna'),('Hounda','Ameze')]
    ve_veriants=models.CharField(max_length=50,unique=True, choices=veriant_type)
    def __str__(self):
        return self.ve_name 

class Fuel(models.Model) :
    fuel_type=[('Petrol','Petrol'),('Desal','Desal'),('CNG','CNG')]
    f_name=models.CharField(max_length=50,choices=fuel_type)  
    ve_name=models.ManyToManyField(Vehicle)
    # ve_veriants=models.ManyToManyField(Vehicle)
    def __str__(self):
        return self.f_name