from django.db import models
# Create your models here.
class StudentDetails(models.Model):
    stdname = models.CharField(max_length=20)
    stdclass = models.IntegerField()
    stdsection = models.CharField(max_length=1)
    joindate = models.DateField()

    def __str__(self):
        return self.stdname