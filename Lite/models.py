from django.db import models
class register(models.Model):
    username=models.CharField(max_length=122)
    height=models.DecimalField( max_digits=5, decimal_places=2)
    weight=models.DecimalField( max_digits=5, decimal_places=2)
    gender=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
# Create your models here.
