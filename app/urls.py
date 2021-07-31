from django.urls import path, include
from .views import SalonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('salons', SalonViewSet, basename='salons')
urlpatterns = [
    path('', include(router.urls)),
]
