from random import choices

from django.db import models

# Create your models here.
from django.db.models.fields import related
from django.template.defaultfilters import first


class DateInfoMixin(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Project(DateInfoMixin, models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(null=True, blank=True)
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )
    project_deadline = models.DateField()

    def __str__(self):
        return self.project_name + " " + str(self.pk)


class Department(DateInfoMixin, models.Model):
    class Meta:
        ordering = ('pk',)

    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=100,
        unique=True,
    )

    def __str__(self):
        return self.name + " (" + str(self.pk) + ")"


JUNIOR = "Junior"
TENURED = "Medium"
SENIOR = "Senior"


class Employee(DateInfoMixin, models.Model):
    class Meta:
        ordering = ('-first_name', 'last_name')

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
    assigned_projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.first_name + " " + self.last_name + " level:" + self.seniority


class AccessCard(DateInfoMixin, models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )
