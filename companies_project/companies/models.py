from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name
