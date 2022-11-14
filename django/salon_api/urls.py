from salon_api.views import VisitViewSet, ServiceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'visits', VisitViewSet, basename='visit')
router.register(r'services', ServiceViewSet, basename='service')

urlpatterns = router.urls
