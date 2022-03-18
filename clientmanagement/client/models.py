

from django.db import models


# Create your models here.

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
    Price = models.FloatField()
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    
