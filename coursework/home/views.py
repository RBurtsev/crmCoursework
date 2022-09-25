from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tasks, Clients, Workers, Parts, Fixes


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_tasks = Tasks.objects.all().count()
    num_clients = Clients.objects.all().count()
    num_workers = Workers.objects.all().count()
    num_fixes = Fixes.objects.all().count()
    num_parts = Parts.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_tasks': num_tasks, 'num_clients': num_clients, 'num_workers': num_workers,
                 'num_fixes': num_fixes, 'num_parts': num_parts},
    )


class PartListView(generic.ListView):
    model = Parts


class BoardListView(generic.ListView):
    model = Parts


class ClientsListView(generic.ListView):
    model = Clients



from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PartCreate(CreateView):
    model = Parts
    fields = '__all__'
    success_url = reverse_lazy('parts')

class PartUpdate(UpdateView):
    model = Parts
    fields = ['name', 'sum', 'average_cost']
    success_url = reverse_lazy('parts')

class PartDelete(DeleteView):
    model = Parts
    success_url = reverse_lazy('parts')

class ClientCreate(CreateView):
    model = Clients
    fields = '__all__'
    success_url = reverse_lazy('clients')

class ClientUpdate(UpdateView):
    model = Clients
    fields = ['full_name', 'mail', 'phone', 'brand_cars', 'numbers_cars']
    success_url = reverse_lazy('clients')

class ClientDelete(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients')

