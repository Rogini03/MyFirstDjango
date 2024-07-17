from django.db import models


# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField
    empname = models.CharField(max_length=12)
    empphone = models.IntegerField
    dateofjoin = models.DateField
    designation = models.CharField(max_length=20)


    def __str__(self):
        return self.empname
