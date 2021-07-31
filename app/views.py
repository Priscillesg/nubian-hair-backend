from rest_framework import viewsets

from .serializers import SalonSerializer, UserSerializer
from .models import Salon
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer