from django.db import models


# Create your models here.
class ProductsModel(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title
