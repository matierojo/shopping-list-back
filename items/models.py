from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.FloatField()
    completed = models.BooleanField(default=False)
