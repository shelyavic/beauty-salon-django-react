from django.contrib import admin

# Register your models here.
from salon_api.models import Service, Visit
# Register your models here.

admin.site.register(Service)
admin.site.register(Visit)