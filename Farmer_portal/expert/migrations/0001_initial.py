# Generated by Django 2.1.5 on 2020-01-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expertlogin',
            fields=[
                ('username', models.CharField(default='hiiiii', max_length=100, primary_key='true', serialize=False)),
                ('password', models.CharField(default='hello', max_length=20)),
                ('category', models.CharField(default='keew', max_length=40)),
                ('email', models.CharField(default='lane1', max_length=50)),
            ],
        ),
    ]