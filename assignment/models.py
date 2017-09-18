from django.db import models

# Create your models here.
class Family(models.Model):
    names = models.CharField(max_length = 20)
    position = models.TextField()
    Description = models.CharField(max_length = 20, default="")
    def __str__ (self):
        return self.names
