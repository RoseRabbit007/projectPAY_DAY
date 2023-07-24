from django.db import models

# Create your models here.
class Bank(models.Model):
    bank_name=models.CharField(max_length=255,blank=False,unique=True)
    bank_code=models.BigIntegerField(unique=True,blank=False)
    branch_name=models.CharField(max_length=255,blank=False)
    account_title=models.CharField(blank=False)
    account_holder_name=models.CharField(max_length=255,blank=False)
    account_number=models.BigIntegerField(unique=True,blank=False)
    text_payer_id=models.CharField(max_length=255,blank=False)



class Address_detail(models.Model):
    address=models.CharField(max_length=255,blank=False)
    area=models.CharField(max_length=255,blank=False)
    city=models.CharField(max_length=255,blank=False)
    state=models.CharField(max_length=255,blank=False)
    zip_code=models.IntegerField(blank=False)
    country=models.CharField(max_length=255,blank=False)
    phone_number=models.BigIntegerField(unique=True,blank=False)
