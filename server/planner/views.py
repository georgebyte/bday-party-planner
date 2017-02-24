from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from planner import models
from planner import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class PartyViewSet(viewsets.ModelViewSet):
    queryset = models.Party.objects.all().prefetch_related('users', 'userrole_set')
    serializer_class = serializers.PartySerializer

    @list_route()
    def latest(self, request):
        try:
            party = models.Party.objects.latest('created_dt')
        except models.Party.DoesNotExist:
            raise Http404('Party entity does not exist')

        serializer = self.get_serializer(party)
        return Response(serializer.data)


class GiftIdeaViewSet(viewsets.ModelViewSet):
    queryset = models.GiftIdea.objects.all().prefetch_related('giftideacomment_set__created_by', 'giftideaupvote_set')
    serializer_class = serializers.GiftIdeaSerializer


class FundContributionViewSet(viewsets.ModelViewSet):
    queryset = models.FundContribution.objects.all().select_related('user')
    serializer_class = serializers.FundContributionSerializer
