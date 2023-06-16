from django.urls import path

from .views import index, create_employee, update_employee, delete_employee

urlpatterns = (
    path('', index, name='index'),

    # todo: add urls for create, update and delete employees
)
