from django.db import models
import random

# Create your models here.


def custom_upload_to(instance, filename):
    batch_no = instance.batch_no
    extension = filename.split('.')[-1]
    new_filename = f"{batch_no}_{random.randint(1, 1000)}.{extension}"
    return f"{batch_no}/{new_filename}"

class Potholes(models.Model):
    batch_no = models.IntegerField(null=True)
    detected = models.BooleanField(default=False)
    image = models.ImageField(upload_to=custom_upload_to, null=True)

class detectedImage(models.Model):
    batch_no = models.IntegerField(null=True)
    image_name = models.CharField(null=True, max_length=100)