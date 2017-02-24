from rest_framework import serializers

from . import models
from . import constants


class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = models.User
        fields = ('id', 'name', 'email', 'birthday')
        read_only_fields = ('id',)


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = models.User
        fields = ('id', 'name', 'email', 'birthday')
        read_only_fields = ('id', 'email')


class UserRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = serializers.SerializerMethodField()

    class Meta(object):
        model = models.UserRole
        fields = ('user', 'role')

    def get_role(self, user_role):
        return {
            'title': constants.USER_ROLE_TITLE[user_role.role],
            'description': constants.USER_ROLE_DESCRIPTION[user_role.role],
        }


class PartySerializer(serializers.ModelSerializer):
    organizers = serializers.SerializerMethodField()
    gift_buyers = serializers.SerializerMethodField()

    class Meta(object):
        model = models.Party
        fields = ('id', 'date', 'deadline', 'organizers', 'gift_buyers')

    def get_organizers(self, party):
        organizers = party.userrole_set.filter(role=constants.UserRoleType.ORGANIZER)
        serializer = UserRoleSerializer(many=True, instance=organizers)
        return serializer.data

    def get_gift_buyers(self, party):
        organizers = party.userrole_set.exclude(role=constants.UserRoleType.ORGANIZER)
        serializer = UserRoleSerializer(many=True, instance=organizers)
        return serializer.data

    def to_representation(self, obj):
        ret = super(PartySerializer, self).to_representation(obj)
        for organizer in ret['organizers']:
            organizer.update(organizer['user'])
            del organizer['user']

        for gift_buyer in ret['gift_buyers']:
            gift_buyer.update(gift_buyer['user'])
            del gift_buyer['user']

        return ret


class GiftIdeaCommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta(object):
        model = models.GiftIdeaComment
        fields = ('id', 'comment', 'created_by', 'created_dt')


class GiftIdeaSerializer(serializers.ModelSerializer):
    comments = GiftIdeaCommentSerializer(many=True, source='giftideacomment_set')
    upvotes = serializers.SerializerMethodField()

    class Meta(object):
        model = models.GiftIdea
        fields = ('id', 'user', 'idea', 'comments', 'upvotes')

    def get_upvotes(self, obj):
        return obj.giftideaupvote_set.count()


class FundContributionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta(object):
        model = models.FundContribution
        fields = ('amount', 'user', 'created_dt')
