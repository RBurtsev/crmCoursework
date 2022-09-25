from django.db import models



class Clients(models.Model):
    full_name = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    brand_cars = models.CharField(max_length=100, default="empty", null=True, blank=True)
    numbers_cars = models.CharField(max_length=20, default="empty", null=True, blank=True)


class Workers(models.Model):
    full_name = models.CharField(max_length=60)
    post = models.CharField(max_length=60)
    password = models.CharField(max_length=100)


class Fixes(models.Model):
    type_active = models.CharField(max_length=60)
    id_car = models.IntegerField()
    id_worker = models.IntegerField()
    id_parts = models.IntegerField()
    repair_cost = models.IntegerField()
    comment = models.CharField(max_length=255)


class Parts(models.Model):
    name = models.CharField(max_length=255)
    sum = models.IntegerField()
    average_cost = models.IntegerField()

class Tasks(models.Model):
    worker_id = models.IntegerField(default=1, null=True, blank=True)
    client_id = models.IntegerField(default=1, null=True, blank=True)
    fix_id = models.IntegerField(default=1, null=True, blank=True)
    parts_id = models.IntegerField(default=1, null=True, blank=True)
    type = models.CharField(max_length=30, default="Test", null=True, blank=True)
