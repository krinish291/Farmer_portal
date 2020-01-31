from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

Category_CHOICES = [
   
    ('Grains','Grains'),
    ('pulses','pulses'),
    ('Vegetables', 'Vegetables'),
    ('Fruits','Fruits'),
    ('Other','Other'),

]


Locations =[
                
               ('Gujrat',
                    (
                        ('Rajkot','Rajkot'),
                        ('Mehsana','Mehsana'),
                        ('Ahmedabad','Ahmedabad'),
                        ('Anand','Anand'),
                        ('Dahod','Dahod'),
                        ('Kheda','Kheda'),
                        ('Vadodara','Vadodara'),
                        ('Panchmahal','Panchmahal'),
                        ('Aravalli','Aravalli'),
                        ('Banaskantha','Banaskantha'),
                        ('Gandhinagar','Gandhinagar'),
                        ('Patan','Patan'),
                        ('Amreli','Amreli'),
                        ('Bhavnagar','Bhavnagar'),
                        ('Jamnagar','Jamnagar'),
                        ('Junagadh','Junagadh'),
                        ('Morbi','Morbi'),                       
                        ('Sabarkantha','Sabarkantha'),
                        ('Bharuch','Bharuch'),
                        ('Dang','Dang'),
                        ('Narmada','Narmada'),
                        ('Navsari','Navsari'),
                        ('Surat','Surat'),
                        ('Valsad','Valsad'),
                    )
               )
            ]

       

Ferti=[
    ('Nofertilizer','Nofertilizer'),
    ('bio-fertilizer','bio-fertilizer'),
    ('Urea','Urea'),
    ('N P K',
        (
            ('NPK 19-19-19','NPK 19-19-19'),
            ('NPK 20-20-20','NPK 20-20-20'),
            ('NPK 20-20-0','NPK 20-20-0'),
            ('NPK 46-0-0','NPK 46-0-0'),
        )
    ),
    ('D A P',
        (
            ('DAP 18-46-0','DAP 18-46-0'),
        )
    ),
    
]
area_type=(
    ('Bigha','Bigha'),
    ('Guntha','Guntha'),
    ('Acre','Acre'),
    ('Hectare','Hectare'),
    ('Square Meter','Square Meter',)
)
def findarea(a):
    i=2*a
    return i


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    Tell_your_story = models.TextField(default="")
    date_posted = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    location = models.CharField(max_length=15, choices=Locations, default='Gujrat')
    seed = models.CharField(max_length=100,default="")
    fertilizers = models.CharField(max_length=15, choices=Ferti, default='Urea')
    treatment_details  = models.TextField(default="") 
    category = models.CharField(max_length=15, choices=Category_CHOICES, default='Grains')   
    Sowing_date = models.DateField(default=timezone.now)
    Harvest_date = models.DateField(default=timezone.now)
    area = models.IntegerField(default="")
    area_type = models.CharField(max_length=15, choices=area_type, default='Bigha')
    net_profit_in_INR_rupee= models.IntegerField(default="")
    image = models.ImageField(default='kisan.jpg', upload_to='Story_pics')
    
   
    #def __str__(self):
     #   return f'{self.user.username} Post' + self.title

    def save(self,*args, **kwargs):
        self.area=findarea(self.area)
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
   