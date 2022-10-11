from django.db import models
from django.utils import timezone
# Create your models here.


class BaseModel(models.Model):
    status = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    modified_at = models.DateTimeField(default=timezone.now, blank=True)
    objects = models.Manager()
    class Meta:
        abstract = True
class Person(BaseModel):
    person=models.CharField(max_length=30,blank=True,null=True)
    class Meta:
        db_table="person"

class Country(BaseModel):
    country_name=models.CharField(max_length=255,default=False,blank=True)
    country_code=models.CharField(max_length=10,default=False,blank=True)
    class Meta:
        db_table="country"

class State(BaseModel):
    country=models.ForeignKey("Country",  on_delete=models.CASCADE)
    state_name=models.CharField(max_length=255,blank=True)
    state_code=models.CharField(max_length=10,blank=True)
    class Meta:
        db_table="state"

class Distric(BaseModel):
    state=models.ForeignKey("State",on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        db_table="distric"

class Pincode(BaseModel):
    distric=models.ForeignKey("Distric",on_delete=models.CASCADE)
    pincode=models.CharField(max_length=15,blank=True,null=True)
    class Meta:
        db_table="pincode"

class Village(BaseModel):
    distric=models.ForeignKey("distric",on_delete=models.CASCADE)
    name=models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        db_table="village"
class Gender(models.Model):
    gender=models.CharField(max_length=10,blank=True)

    class Meta:
        db_table="gender"


class Register(BaseModel):
    user_id=models.CharField(max_length=25,default=False)
    first_name=models.CharField(max_length=55,default=False)
    last_name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=50,default=False)
    mobile=models.CharField(max_length=15,blank=True)
    # date_of_birthday=models.DateField( models.AutoField(_("")))
    create_by=models.ForeignKey("Person",on_delete=models.CASCADE)
    password=models.CharField(max_length=600,blank=True)
    gender=models.ForeignKey("Gender",on_delete=models.CASCADE)
    class Meta:
        db_table="register"



class Test(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=10,blank=True,null=True)
    class Meta:
        db_table="test"


