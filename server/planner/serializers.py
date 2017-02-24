from rest_framework import serializers

from . import models


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

    class Meta(object):
        model = models.UserRole
        fields = ('user', 'role')


class PartySerializer(serializers.ModelSerializer):
    users = UserRoleSerializer(many=True, source='userrole_set')

    class Meta(object):
        model = models.Party
        fields = ('id', 'date', 'deadline', 'users')


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
