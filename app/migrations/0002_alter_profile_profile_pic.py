# Generated by Django 4.2 on 2023-05-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_pic',
            field=models.ImageField(upload_to='Profile_Pics'),
        ),
    ]
