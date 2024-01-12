from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    

