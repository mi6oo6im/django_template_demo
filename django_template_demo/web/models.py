from django.db import models

# Create your models here.
from django.template.defaultfilters import first


class Department(models.Model):
    name = models.CharField(max_length=20)


class Employee(models.Model):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    middle_name = models.CharField(max_length=10, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_address = models.EmailField()
