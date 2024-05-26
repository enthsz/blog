from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='fotos/padrao.jpg', upload_to='fotos', null=True, blank=True)


    
    def is_default_image(self):
        return self.image.name == 'fotos/padrao.jpg'

    def delete_old_image(self):
        if self.image and not self.is_default_image():
            image_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            if os.path.exists(image_path):
                os.remove(image_path)






    def __str__(self):
        return f'{self.user.username} Profile' 