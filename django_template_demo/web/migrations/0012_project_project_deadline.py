# Generated by Django 4.2.2 on 2023-06-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_project_employee_assigned_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_deadline',
            field=models.DateField(default='2023-12-31'),
            preserve_default=False,
        ),
    ]
