from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Myservice(models.Model):
    email = models.EmailField(primary_key=True)
    service_details = models.TextField()