from django.urls import path, include
from .views import SalonViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('salons', SalonViewSet, basename='salons')
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
