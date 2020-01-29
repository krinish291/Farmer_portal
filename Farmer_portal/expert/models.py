from django.db import models

class expertlogin(models.Model):
    username = models.CharField(max_length=100,default='hiiiii', primary_key='true')
    password = models.CharField(max_length=20,default='hello')
    category= models.CharField(max_length=40,default='keew')
    email = models.CharField(max_length=50,default='lane1'   )
    
    