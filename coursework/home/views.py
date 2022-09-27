from django.shortcuts import render
from django.views import generic

from .models import Clients, Workers, Parts, Fixes


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_clients = Clients.objects.all().count()
    num_workers = Workers.objects.all().count()
    num_fixes = Fixes.objects.all().count()
    num_parts = Parts.objects.all().count()
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_clients': num_clients, 'num_workers': num_workers,
                 'num_fixes': num_fixes, 'num_parts': num_parts},
    )

def top_clients_array():
    top_clients = []
    help_top_clients = {}
    for e in Fixes.objects.all():
        try:
            help_top_clients[e.id_car] += 1
        except:
            help_top_clients[e.id_car] = 1
    sorted_help_clients = dict(sorted(help_top_clients.items(), key=lambda item: item[1]))
    for key, value in sorted_help_clients.items():
        top_clients.append([key, value])
    top_clients = top_clients[::-1]
    if len(top_clients) > 5:
        top_clients = top_clients[:5]
    for e in Clients.objects.all():
        for i in range(len(top_clients)):
            if top_clients[i][0] == int(e.id):
                top_clients[i][0] = e.full_name
    return top_clients

def top_workers_array():
    top_workers = []
    help_top_workers = {}
    for e in Fixes.objects.all():
        try:
            help_top_workers[e.id_worker] += 1
        except:
            help_top_workers[e.id_worker] = 1
    sorted_help_workers = dict(sorted(help_top_workers.items(), key=lambda item: item[1]))
    for key, value in sorted_help_workers.items():
        top_workers.append([key, value])
    top_workers = top_workers[::-1]
    if len(top_workers) > 5:
        top_workers = top_workers[:5]
    for e in Workers.objects.all():
        for i in range(len(top_workers)):
            if top_workers[i][0] == int(e.id):
                top_workers[i][0] = e.full_name
    return top_workers

def all_parts():
    numbers_all = 0
    cost_all_parts = 0
    for e in Parts.objects.all():
        cost_all_parts += e.sum * e.average_cost
        numbers_all += e.sum
    average_cost_all = cost_all_parts / numbers_all
    return [numbers_all, cost_all_parts, average_cost_all]

def managedeck(request):
    num_clients = Clients.objects.all().count()
    num_workers = Workers.objects.all().count()
    num_fixes = Fixes.objects.all().count()
    num_parts = Parts.objects.all().count()
    top_clients = top_clients_array()
    top_workers = top_workers_array()
    for_parts = all_parts()
    numbers_all_parts = for_parts[0]
    cost_all_parts = for_parts[1]
    average_cost_all_parts = round(for_parts[2])
    return render(
        request,
        'managedeck.html',
        context={'num_clients': num_clients, 'num_workers': num_workers,
                 'num_fixes': num_fixes, 'num_parts': num_parts,
                 'top_clients': top_clients, 'top_workers': top_workers,
                 'numbers_all_parts': numbers_all_parts, 'cost_all_parts': cost_all_parts, 'average_cost_all_parts': average_cost_all_parts},
    )

class PartListView(generic.ListView):
    model = Parts


class ClientsListView(generic.ListView):
    model = Clients


class FixesListView(generic.ListView):
    model = Fixes


class WorkersListView(generic.ListView):
    model = Workers



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

class FixesCreate(CreateView):
    model = Fixes
    fields = '__all__'
    success_url = reverse_lazy('fixes')

class FixesUpdate(UpdateView):
    model = Fixes
    fields = ['type_active', 'id_car', 'id_worker', 'id_parts', 'repair_cost', 'comment']
    success_url = reverse_lazy('fixes')

class FixesDelete(DeleteView):
    model = Fixes
    success_url = reverse_lazy('fixes')


class WorkersCreate(CreateView):
    model = Workers
    fields = '__all__'
    success_url = reverse_lazy('workers')

class WorkersUpdate(UpdateView):
    model = Workers
    fields = ['full_name', 'post', 'password']
    success_url = reverse_lazy('workers')

class WorkersDelete(DeleteView):
    model = Workers
    success_url = reverse_lazy('workers')


