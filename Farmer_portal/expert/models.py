from django.db import models
from django.contrib.auth.models import User
from _queue import SimpleQueue

Category_CHOICES = [
   
    ('Grains','Grains'),
    ('pulses','pulses'),
    ('Vegetables', 'Vegetables'),
    ('Fruits','Fruits'),
    ('Other','Other'),

]
class Expert(models.Model):   
    username = models.CharField(max_length=100,default='',unique=True)
    password = models.CharField(max_length=20,default='')
    Dp = models.ImageField(default='kisan.jpg', upload_to='Expert_pics')
    category= models.CharField(max_length=15, choices=Category_CHOICES, default='Grains')
    email = models.EmailField(max_length=50,default='' )
    File_Verify =models.FileField(upload_to='documents/')
    description = models.TextField(default="") 
    is_valid = models.BooleanField(default=False)
    
