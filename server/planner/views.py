from rest_framework import viewsets

from planner import models
from planner import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = models.Party.objects.all().prefetch_related('users', 'userrole_set')
    serializer_class = serializers.PartySerializer
