from django.urls import path, include

from .views import index, create_employee, update_employee, delete_employee

urlpatterns = (
    path('', index, name='index'),
    # todo: add urls for create, update and delete employees and departments
    # path('department/', include(
    #     path('all/', show_departmetns, name='departments list'),
    #     path('create/', create_department, name='create department')
    # )


)
