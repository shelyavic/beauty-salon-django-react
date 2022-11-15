from datetime import datetime

from django.conf import settings
from django.utils.translation import gettext as _

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView

from rest_framework import permissions
from rest_framework.permissions import AllowAny, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from salon_api.models import Visit, Service
from salon_api.serializers import (
    ClientVisitSerializer,
    MasterVisitSerializer,
    ServiceSerializer,
)
from salon_api.utils import has_group


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.client == request.user


class IsMaster(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return has_group(request.user, settings.MASTER_GROUP_NAME)


class IsAccountOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.kwargs["pk"] == request.user.id


class VisitViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                AllowAny,
            ]
        else:
            permission_classes = [IsOwner | IsMaster]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Visit.objects.all()

    def get_serializer_class(self):
        if has_group(self.request.user, settings.MASTER_GROUP_NAME):
            return MasterVisitSerializer
        else:
            return ClientVisitSerializer

    def check_time_interception(self, serializer, object2exclude=None):
        new_date_time = serializer.validated_data.get("date_time")
        new_service = serializer.validated_data.get("service")

        if new_date_time.date() <= datetime.now().date():
            raise ValidationError(
                {"date_time": _("Сan't create an entry for a past date")}
            )

        visits_date = Visit.objects.filter(date_time__date=new_date_time.date())
        if object2exclude:
            visits_date = visits_date.exclude(id=object2exclude.id)

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
        self.check_time_interception(serializer, object2exclude=self.get_object())
        serializer.save()


class RetriveUserVisits(RetrieveAPIView):
    serializer_class = ClientVisitSerializer
    queryset = Visit.objects.all()
    permission_classes = [IsAccountOwner]

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs["pk"]
        queryset = Visit.objects.filter(client_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceViewSet(ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
