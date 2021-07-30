from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from apps.authentication.models.user_manager import UserManager
from apps.core.models import TimeStampedAbstractModel


class User(AbstractUser, TimeStampedAbstractModel):
    """ model that reprsent user """
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.username
