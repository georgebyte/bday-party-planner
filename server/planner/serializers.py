from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = models.User
        fields = ('id', 'url', 'email', 'birthday')
