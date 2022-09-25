from django.contrib import admin
from .models import Tasks, Clients, Workers, Fixes, Parts

admin.site.register(Tasks)
admin.site.register(Clients)
admin.site.register(Workers)
admin.site.register(Fixes)
admin.site.register(Parts)

