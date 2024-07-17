from django.db import models


# Create your models here.
class Admission(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    course = models.CharField(max_length=5)
    joindate = models.DateField()

    def __str__(self):
        return self.name