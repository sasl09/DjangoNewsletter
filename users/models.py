from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from PIL import Image
=======
<<<<<<< HEAD
from PIL import Image
=======
<<<<<<< HEAD
from PIL import Image
=======
<<<<<<< HEAD
from PIL import Image
=======
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
>>>>>>> 6fbf1c87481d04d8b2b9e4646d7dee9dd692d903
>>>>>>> 4a51a5607dbdc881353c89d80ffa8b61fbfb97fd
>>>>>>> 83dc61fee60c4eba1255746d125f42f15fceaa24
>>>>>>> d60f817bc5b4c51445fc8a176c2960a3e9e5a9a2


