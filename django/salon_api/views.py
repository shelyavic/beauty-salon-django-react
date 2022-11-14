from datetime import datetime
from django.conf import settings
from django.utils.translation import gettext as _

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from salon_api.models import Visit, Service
from salon_api.serializers import (
    ClientVisitSerializer,
    MasterVisitSerializer,
    ServiceSerializer,
)
from salon_api.utils import has_group


def check_time_interception(serializer, exclude_object=None):
    new_date_time = serializer.data.get("date_time")
    new_service = serializer.data.get("service")

    if new_date_time.date() <= datetime.now().date():
        raise ValidationError({"date_time": _("Сan't create an entry for a past date")})

    visits_date = Visit.objects.filter(date_time__date=new_date_time.date())
    if exclude_object:
        visits_date = visits_date.exclude(id=exclude_object.id)

    for visit in visits_date:
        if (
            visit.date_time < new_date_time < visit.end_date_time
            or visit.date_time
            < (new_date_time + new_service.duration)
            < visit.end_date_time
        ):
            raise ValidationError(
                {"date_time": _("Requested date and time are already taken")}
            )

class VisitViewSet(ModelViewSet):
    
    def get_queryset(self):
        return Visit.objects.all()

    def get_serializer_class(self):
        if has_group(self.request.user, settings.MASTER_GROUP_NAME):
            return MasterVisitSerializer
        else:
            return ClientVisitSerializer

    def filter_queryset(self, queryset):
        """Is used in create(), update(), destroy() methods"""
        if not has_group(self.request.user, settings.MASTER_GROUP_NAME):
            queryset = queryset.filter(client=self.request.user)
        return queryset

    def check_time_interception(self, serializer, exclude_object=None):
        new_date_time = serializer.data.get("date_time")
        new_service = serializer.data.get("service")

        if new_date_time.date() <= datetime.now().date():
            raise ValidationError({"date_time": _("Сan't create an entry for a past date")})

        visits_date = Visit.objects.filter(date_time__date=new_date_time.date())
        if exclude_object:
            visits_date = visits_date.exclude(id=exclude_object.id)

        for visit in visits_date:
            if (
                visit.date_time < new_date_time < visit.end_date_time
                or visit.date_time
                < (new_date_time + new_service.duration)
                < visit.end_date_time
            ):
                raise ValidationError(
                    {"date_time": _("Requested date and time are already taken")}
                )


    def perform_create(self, serializer):
        self.check_time_interception(serializer)
        if not has_group(self.request.user, settings.MASTER_GROUP_NAME):
            serializer.save(client=self.request.user)
        else:
            serializer.save()

    def perform_update(self, serializer):
        self.check_time_interception(serializer, exclude_object=self.get_object())
        serializer.save()




class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


