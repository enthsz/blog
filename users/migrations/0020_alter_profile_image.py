# Generated by Django 5.0.6 on 2024-05-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='fotos/padrao.jpg', null=True, upload_to='fotos'),
        ),
    ]
