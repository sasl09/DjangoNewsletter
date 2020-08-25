from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from PIL import Image
=======
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
<<<<<<< HEAD

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
=======
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903


