from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser

class FoodDonate(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    phone = models.IntegerField(validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999)
        ])
    food_cat = models.CharField(max_length=10)
    address = models.TextField()
    description = models.TextField()
    no_of_people = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class RequestFood(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    food = models.ForeignKey(FoodDonate,on_delete=models.CASCADE,null=True)