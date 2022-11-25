from django.urls import include, path
from salon_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'visits', views.VisitViewSet, basename='visit')
router.register(r'services', views.ServiceViewSet, basename='service')

urlpatterns = [
    path(r'', include(router.urls)),
    path('users/<int:pk>/visits/', views.RetriveUserVisits.as_view()),
    path('users/me/', views.CurrentUser.as_view()),
    
]