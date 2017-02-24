from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = models.User
        fields = ('id', 'name', 'email', 'birthday')


class UserRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta(object):
        model = models.UserRole
        fields = ('user', 'role')


class PartySerializer(serializers.ModelSerializer):
    users = UserRoleSerializer(many=True, source='userrole_set')

    class Meta(object):
        model = models.Party
        fields = ('id', 'date', 'deadline', 'users')
