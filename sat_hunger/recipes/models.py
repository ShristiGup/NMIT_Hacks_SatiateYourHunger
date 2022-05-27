from django.db import models
from users.models import *
from datetime import datetime
from PIL import Image
# Create your models here.
class RecentSearches(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    ingredients = models.CharField(max_length=1000)
    food_cat = models.CharField(max_length=20)
    hunger_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s Search"

    class Meta: 
        verbose_name_plural = 'RecentSearches'


APPROVAL_CHOICES = (
    ('approved', 'approved'),
    ('rejected', 'rejected'),
    ('pending', 'pending'),
)
class AddedRecipe(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=400)
    ingredients = models.TextField()
    steps = models.TextField()
    healthScore = models.PositiveIntegerField(default=10)
    readyInMinutes = models.PositiveIntegerField(default=10)
    food_cat = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    youTubeId = models.TextField(null=True, blank=True)
    approval = models.CharField(max_length=20, choices=APPROVAL_CHOICES, default="pending")
    timestamp = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    recipe = models.ForeignKey(AddedRecipe, on_delete=models.CASCADE, null=False)
    text = models.TextField()