from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='이메일',
        null=False
    )
    name = models.CharField(
        verbose_name='이름',
        max_length=255,
        null=False,
        blank=False
    )
