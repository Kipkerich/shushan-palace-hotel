from PIL import Image
from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    size = models.CharField(max_length=200, blank=False, null=False)
    price = models.CharField(max_length=150, blank=False, null=False)
    desc = models.CharField(max_length=400, blank=False, null=False)
    image = models.ImageField(upload_to ='static/assets/img/rooms/')

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 500 or img.width < 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)


def __str__(self):
    return self.name
