from django.db import models

# Create your models here.
gender_choice=[
    ('male','male'),
    ('female','femail')
]

class personal_detail_model(models.Model):
    first_name=models.CharField(max_length=100,blank=False)
    last_name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(blank=False,unique=True)
    emp_id=models.CharField(unique=True,blank=False)
    phone_no=models.BigIntegerField(unique=True,blank=False)
    gender=models.CharField(choices=gender_choice)
    birthday=models.CharField(blank=False)
    AboutMe=models.CharField(max_length=300,blank=False)
    
class Document_model(models.Model):
    name=models.CharField(max_length=100,blank=False)
    Document=models.FileField(upload_to='document/')

class emergency_contact(models.Model):
    name=models.CharField(max_length=100,blank=False)
    address=models.CharField(max_length=100,blank=False)
    relationship=models.CharField(max_length=100,blank=False)
    city=models.CharField(max_length=100,blank=False)
    phonenumber=models.BigIntegerField(blank=False,unique=True)
    country=models.CharField(max_length=10,blank=False)
    email=models.CharField(max_length=100,blank=False,unique=True)
    
class salary(models.Model):
    name=models.CharField(max_length=100,blank=False)
    salary=models.IntegerField(blank=False)

class socialmedialink(models.Model):
    name=models.CharField(max_length=100,blank=False)
    social_meadia=models.URLField(blank=False)