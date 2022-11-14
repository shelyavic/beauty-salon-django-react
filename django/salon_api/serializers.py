from rest_framework.serializers import ModelSerializer

from salon_api.models import Visit, Service


class ClientVisitSerializer(ModelSerializer):
    class Meta:
        model = Visit
        exclude = ['client']


class MasterVisitSerializer(ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"
