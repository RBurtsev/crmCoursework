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
    BACKLOG = "BL"
    TO_DO = "TD"
    IN_PROGRESS = "IP"
    DONE = "DE"
    TYPE = [
        ('BL', 'Backlog'),
        ('TD', 'To_do'),
        ('IP', 'In_progress'),
        ('DE', 'Done')

    ]
    type_active = models.CharField(
        max_length=2,
        choices=TYPE,
        default=BACKLOG
    )
    id_car = models.IntegerField()
    id_worker = models.IntegerField()
    id_parts = models.IntegerField()
    repair_cost = models.IntegerField()
    comment = models.CharField(max_length=255)


class Parts(models.Model):
    name = models.CharField(max_length=255)
    sum = models.IntegerField()
    average_cost = models.IntegerField()

