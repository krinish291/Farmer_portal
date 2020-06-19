# Generated by Django 2.1.5 on 2020-02-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=20)),
                ('Dp', models.ImageField(default='kisan.jpg', upload_to='Expert_pics')),
                ('category', models.CharField(choices=[('Grains', 'Grains'), ('pulses', 'pulses'), ('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Other', 'Other')], default='Grains', max_length=15)),
                ('email', models.EmailField(default='', max_length=50)),
                ('File', models.FileField(upload_to='documents/')),
                ('description', models.EmailField(blank=True, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='gunjan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]