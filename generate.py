import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyDjangoFirstApplication.settings')

import django
django.setup()

from SecondApp.models import StudentDetails
from IndigoApp.models import Admission

from random import *
from faker import Faker
faker = Faker()

def generatefakerdatas():
    f_name=faker.name()
    f_class=randint(5,12)
    f_section='A'
    f_date=faker.date_object()
    StudentDetails.objects.get_or_create(stdname=f_name,
                                         stdsection=f_section,
                                        stdclass=f_class,
                                        joindate=f_date)
for i in range(0,10):
    generatefakerdatas()

def generateadmision():
    a_name=faker.name()
    a_email = faker.email()
    a_course= "MBBS"
    a_date=faker.date_object()
    Admission.objects.get_or_create(name=a_name,
                                    email=a_email,
                                    course=a_course,
                                    joindate = a_date)
for i in range(0,10):
    generateadmision()

