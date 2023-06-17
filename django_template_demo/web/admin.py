from django.contrib import admin

# Register your models here.
from django_template_demo.web.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'department', 'created_on')
