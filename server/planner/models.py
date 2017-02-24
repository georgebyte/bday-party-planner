from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from . import constants


class User(AbstractBaseUser):
    birthday = models.DateField()


class Party(models.Model):
    date = models.DateField(null=True)
    date_from = models.DateField()
    date_to = models.DateField()

    users = models.ManyToManyField(User, through='UserRole')


class UserRole(models.Model):
    user = models.ForeignKey(User)
    party = models.ForeignKey(Party)

    role = models.PositiveSmallIntegerField(choices=constants.UserRoleType.get_choices())
