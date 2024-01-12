from django.db import models

class Logindb(models.Model):
    name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=10)
