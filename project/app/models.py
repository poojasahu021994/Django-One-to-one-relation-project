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
