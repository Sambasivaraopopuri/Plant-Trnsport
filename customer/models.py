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

class Referral(BaseModel):
    customer=models.ForeignKey("Customer",on_delete=models.CASCADE)
    referral_id=models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        db_table="referral"

class Customer(BaseModel):
    first_name=models.CharField(max_length=500,blank=True)
    last_name=models.CharField(max_length=500,blank=True)
    gender=models.ForeignKey("master.Gender",on_delete=models.CASCADE)
    email=models.EmailField(blank=True,null=True)
    mobile=models.CharField(max_length=500,blank=True,null=True)
    country=models.ForeignKey("master.Country",on_delete=models.CASCADE)
    state=models.ForeignKey("master.State",on_delete=models.CASCADE)
    distric=models.ForeignKey("master.Distric",on_delete=models.CASCADE)
    village=models.ForeignKey("master.village",on_delete=models.CASCADE)
    pincode=models.ForeignKey("master.Pincode",on_delete=models.CASCADE)
    customer_id=models.CharField(max_length=20,blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    class Meat:
        db_table="customer"


