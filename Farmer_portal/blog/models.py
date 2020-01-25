from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


Category_CHOICES = (
    ('Grains','Grains'),
    ('pulses','pulses'),
    ('Vegetables', 'Vegetables'),
    ('Fruits','Fruits'),
    ('Other','Other'),
    
)


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100,default="")
    seed = models.CharField(max_length=100,default="")
    fertilizers = models.CharField(max_length=100,default="")
    treatment_details  = models.TextField(default="") 
    category = models.CharField(max_length=15, choices=Category_CHOICES, default='Grains')   
    Sowing_date = models.DateField(default=timezone.now)
    Harvest_date = models.DateField(default=timezone.now)
    area = models.CharField(max_length=123,default="")
    net_profit = models.CharField(max_length=123,default="")
    image = models.ImageField(default='kisan.jpg', upload_to='Story_pics')
    
    def timeduraction(self):
        return (Sowing_date - Harvest_date)
    #def __str__(self):
     #   return f'{self.user.username} Post' + self.title

    def save(self,*args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Post_id = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name="likes")
   