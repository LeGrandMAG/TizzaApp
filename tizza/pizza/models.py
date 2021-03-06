from django.db import models

from django.contrib.auth.models  import User 
# Create your models here.


class Pizzeria(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)

class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    approved = models.BooleanField(default= False)
    creator = models.ForeignKey(Pizzeria, on_delete=models.CASCADE, null=True)

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)






