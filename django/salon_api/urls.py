from django.urls import include, path
from salon_api.views import VisitViewSet, ServiceViewSet, RetriveUserVisits
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'visits', VisitViewSet, basename='visit')
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'users/<int:pk>/visits/', RetriveUserVisits.as_view()),
    
]