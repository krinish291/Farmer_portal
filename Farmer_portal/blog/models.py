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
    category = models.CharField(max_length=15, choices=Category_CHOICES, default='Grains')
    image = models.ImageField(default='kisan.jpg', upload_to='Story_pics')
    blogtype=models.CharField(max_length=500)
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