from rest_framework.serializers import ModelSerializer, SerializerMethodField
from salon_api.utils import has_group
from django.conf import settings
from salon_api.models import Visit, Service
from django.contrib.auth import get_user_model

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


class UserInfoSerializer(ModelSerializer):
    is_master = SerializerMethodField()
    class Meta:
        model = get_user_model()
        fields = ["id", "email", 'is_master']
    
    def get_is_master(self, obj):
        return has_group(obj, settings.MASTER_GROUP_NAME)