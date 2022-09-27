from django.contrib import admin
from .models import Clients, Workers, Fixes, Parts

admin.site.register(Clients)
admin.site.register(Workers)
admin.site.register(Fixes)
admin.site.register(Parts)

