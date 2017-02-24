from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from . import constants


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        user = self.model(
            email=email,
            is_superuser=is_superuser,
            last_login=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    birthday = models.DateField()
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['birthday']

    objects = UserManager()


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
