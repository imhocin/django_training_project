from django.db import models
import random
import os


# Create your models here.


def get_file_extension(filename):

    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):

    name, ext = get_file_extension(filename)
    rand = random.randint(100, 999)
    return f"products/{instance.title}-{rand}-{name}.{ext}"


class ProductsModel(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)

    def __str__(self):
        return self.title
