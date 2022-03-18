

from xmlrpc.client import boolean
from django.db import models


# Create your models here.

PAID_CHOICES = (
    ("Paid", "Paid"),
    ("Not Paid", "Not Paid"),

)

class Industry(models.Model):
   name = models.CharField(max_length = 150 , null=True)
   
   def __str__(self):
       return self.name
   

class Client(models.Model):
    name= models.CharField(max_length=150, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
class ServicesCategory(models.Model):
    name=models.CharField(max_length=150, null=True)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name= models.CharField(max_length = 150 ,null='True')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    service_category = models.ForeignKey(ServicesCategory, on_delete=models.CASCADE, null=True)
    date_started = models.DateField(auto_now=False, auto_now_add=False, null=True)
    date_ended = models.DateField(auto_now=False, auto_now_add=False, null=True)
    date_expired = models.DateField(auto_now=False, auto_now_add=False, null=True)
    paid_status = models.CharField(max_length = 150, choices=PAID_CHOICES, default='Not Paid')
    
    Price = models.FloatField()
    
    def __str__(self):
        return self.name
    
    
class Payment(models.Model):
    name = models.CharField(max_length = 150)
    amount_paid=models.FloatField()
    date_paid = models.DateField(auto_now=False, auto_now_add=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
       
       return self.name
    
    
    
    
    
    
    
    
    
    
    
