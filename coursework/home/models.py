from django.db import models


class Tasks(models.Model):
    id_worker = models.IntegerField()
    id_client = models.IntegerField()
    id_fix = models.IntegerField()
    type = models.CharField(max_length=60)


class Clients(models.Model):
    full_name = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)


class Cars(models.Model):
    number = models.CharField(max_length=20)
    id_client = models.IntegerField()


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
    type_active = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    sum = models.IntegerField()
    average_cost = models.IntegerField()
