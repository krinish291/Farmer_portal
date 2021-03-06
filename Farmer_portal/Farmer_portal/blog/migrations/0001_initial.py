# Generated by Django 2.1.5 on 2020-02-02 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Tell_your_story', models.TextField(default='')),
                ('date_posted', models.DateField(auto_now=True)),
                ('location', models.CharField(choices=[('Gujrat', (('Rajkot', 'Rajkot'), ('Mehsana', 'Mehsana'), ('Ahmedabad', 'Ahmedabad'), ('Anand', 'Anand'), ('Dahod', 'Dahod'), ('Kheda', 'Kheda'), ('Vadodara', 'Vadodara'), ('Panchmahal', 'Panchmahal'), ('Aravalli', 'Aravalli'), ('Banaskantha', 'Banaskantha'), ('Gandhinagar', 'Gandhinagar'), ('Patan', 'Patan'), ('Amreli', 'Amreli'), ('Bhavnagar', 'Bhavnagar'), ('Jamnagar', 'Jamnagar'), ('Junagadh', 'Junagadh'), ('Morbi', 'Morbi'), ('Sabarkantha', 'Sabarkantha'), ('Bharuch', 'Bharuch'), ('Dang', 'Dang'), ('Narmada', 'Narmada'), ('Navsari', 'Navsari'), ('Surat', 'Surat'), ('Valsad', 'Valsad')))], default='Gujrat', max_length=15)),
                ('seed', models.CharField(default='', max_length=100)),
                ('fertilizers', models.CharField(choices=[('Nofertilizer', 'Nofertilizer'), ('bio-fertilizer', 'bio-fertilizer'), ('Urea', 'Urea'), ('N P K', (('NPK 19-19-19', 'NPK 19-19-19'), ('NPK 20-20-20', 'NPK 20-20-20'), ('NPK 20-20-0', 'NPK 20-20-0'), ('NPK 46-0-0', 'NPK 46-0-0'))), ('D A P', (('DAP 18-46-0', 'DAP 18-46-0'),))], default='Urea', max_length=15)),
                ('treatment_details', models.TextField(default='')),
                ('category', models.CharField(choices=[('Grains', 'Grains'), ('pulses', 'pulses'), ('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Other', 'Other')], default='Grains', max_length=15)),
                ('Sowing_date', models.DateField(default=django.utils.timezone.now)),
                ('Harvest_date', models.DateField(default=django.utils.timezone.now)),
                ('area', models.IntegerField(default='')),
                ('area_type', models.CharField(choices=[('Bigha', 'Bigha'), ('Guntha', 'Guntha'), ('Acre', 'Acre'), ('Hectare', 'Hectare'), ('Square Meter', 'Square Meter')], default='Bigha', max_length=15)),
                ('net_profit_in_INR_rupee', models.IntegerField(default='')),
                ('image', models.ImageField(default='kisan.jpg', upload_to='Story_pics')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Grains', 'Grains'), ('pulses', 'pulses'), ('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Other', 'Other')], default='Grains', max_length=15)),
                ('image', models.ImageField(default='kisan.jpg', upload_to='query_pics')),
                ('Tell_your_Query', models.TextField(default='')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='Post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
