from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'common/index.html')


def create_employee(request):
    pass


def update_employee(request, pk):
    pass


def delete_employee(request, pk):
    pass


def create_department(request):
    pass


def update_department(request, pk):
    pass


def delete_department(request, pk):
    pass
