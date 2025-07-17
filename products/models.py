from django.db import models
import random
import os
from django.utils.text import slugify


# Create your models here.


def get_file_extension(filename):

    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image(instance, filename):

    name, ext = get_file_extension(filename)
    rand = random.randint(100, 999)
    return f"products/{instance.title}-{rand}-{name}.{ext}"


class ObjectManager(models.Manager):

    def get_object_by_id(self, id):
        product = ProductsModel.objects.filter(id=id)
        return product.first()

    def all(self):
        return ProductsModel.objects.filter(status=True)


class ProductsModel(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to=upload_image, null=True, blank=True)
    status = models.BooleanField(null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    objects = ObjectManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.description)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
