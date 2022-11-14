from rest_framework.viewsets import ModelViewSet
from salon_api.serializers import MasterVisitSerializer
from salon_api.models import Visit, Service


class VisitViewSet(ModelViewSet):
    def get_serializer_class(self):
        return MasterVisitSerializer
    
    def get_queryset(self):
        return Visit.objects.all()

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    
