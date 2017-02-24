from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from . import constants


class User(AbstractBaseUser):
    birthday = models.DateField()
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthday']


class Party(models.Model):
    date = models.DateField(null=True)

    date_from = models.DateField()
    date_to = models.DateField()

    users = models.ManyToManyField(User, through='UserRole')


class UserRole(models.Model):
    user = models.ForeignKey(User)
    party = models.ForeignKey(Party)

    role = models.PositiveSmallIntegerField(choices=constants.UserRoleType.get_choices())


class PresentIdea(models.Model):
    user = models.ForeignKey(User)
    idea = models.TextField()

    party_used = models.ForeignKey(Party, null=True, blank=True)

    created_by = models.ForeignKey(User, related_name='+')
    created_dt = models.DateTimeField(auto_now_add=True)


class PresentIdeaComment(models.Model):
    idea = models.ForeignKey(PresentIdea)
    comment = models.TextField()

    created_by = models.ForeignKey(User, related_name='+')
    created_dt = models.DateTimeField(auto_now_add=True)


class PresentIdeaUpvote(models.Model):
    idea = models.ForeignKey(PresentIdea)

    created_by = models.ForeignKey(User, related_name='+')
    created_dt = models.DateTimeField(auto_now_add=True)


class FundContribution(models.Model):
    user = models.ForeignKey(User)
    amount = models.IntegerField()

    created_dt = models.DateTimeField(auto_now_add=True)
