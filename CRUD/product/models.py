from django.db import models

# Create your models here.
class product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    category = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    images = models.URLField(max_length=500, null=True)

    def __str__(self):
        return self.id
