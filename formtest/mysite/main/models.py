from django.db import models

# Create your models here.
class Car(models.Model):
  name = models.CharField(max_length=100)
  year = models.DecimalField(max_digits=4, decimal_places= 0)
  hp = models.DecimalField(max_digits=4, decimal_places= 0)
  top_speed_mph = models.DecimalField(max_digits=3, decimal_places= 0)
  weight_kg = models.DecimalField(max_digits=4, decimal_places= 0)