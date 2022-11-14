from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Service(models.Model):
    name = models.CharField(_("Service name"), max_length=255)
    duration = models.DurationField(_('Duration in seconds'))
    
    def __str__(self):
        return self.name


class Visit(models.Model):
    date_time = models.DateTimeField(_("Date and time of visit"))
    client_note = models.CharField(_("Client's note"), blank=True, max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def end_date_time(self):
        return self.date_time + self.service.duration
    
    def __str__(self):
        return str(self.date_time)