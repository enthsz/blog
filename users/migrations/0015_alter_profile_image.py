# Generated by Django 5.0.6 on 2024-05-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]