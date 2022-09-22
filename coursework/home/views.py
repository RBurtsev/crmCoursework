from django.shortcuts import render
from django.views import generic
from .models import Tasks, Clients, Cars, Workers, Parts, Fixes


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_tasks = Tasks.objects.all().count()
    num_clients = Clients.objects.all().count()
    num_cars = Cars.objects.all().count()
    num_workers = Workers.objects.all().count()
    num_fixes = Fixes.objects.all().count()
    num_parts = Parts.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_tasks': num_tasks, 'num_clients': num_clients, 'num_cars': num_cars, 'num_workers': num_workers,
                 'num_fixes': num_fixes, 'num_parts': num_parts},
    )

class PartListView(generic.ListView):
    model = Parts

class BoardListView(generic.ListView):
    model = Parts

class ClientsListView(generic.ListView):
    model = Clients


