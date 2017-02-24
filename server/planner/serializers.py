from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = models.User
        fields = ('id', 'name', 'email', 'birthday')


class PartySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = models.Party
        fields = ('id', 'date', 'date_from', 'date_to', 'users')
