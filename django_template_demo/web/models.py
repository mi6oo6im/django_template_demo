from random import choices

from django.db import models

# Create your models here.
from django.template.defaultfilters import first


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name + " " + str(self.pk)


JUNIOR = "Junior"
TENURED = "Medium"
SENIOR = "Senior"


class Employee(models.Model):

    class Meta:
        sort_order = ('first_name', '-last_name')

    EXPERIENCE_LEVEL = (
        (
            JUNIOR, JUNIOR
        ),
        (
            TENURED, TENURED
        ),
        (
            SENIOR, SENIOR
        ),
    )
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    middle_name = models.CharField(max_length=10, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email_address = models.EmailField()
    seniority = models.CharField(choices=EXPERIENCE_LEVEL, max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name + " level:" + self.seniority
