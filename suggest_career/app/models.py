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
    user_type = models.CharField(
        verbose_name='유저 유형',
        max_length=255,
        null=False,
        blank=False
    )
    mbti = models.CharField(
        verbose_name='MBTI',
        max_length=255,
        null=False,
        blank=False
    )


class TestHistory(models.Model):
    user = models.ForeignKey(
        verbose_name='테스트한 유저',
        to=User,
        on_delete=models.CASCADE,
        null=False,
        related_name='history_user'
    )
    result = models.CharField(
        verbose_name='테스트',
        max_length=255,
        null=False,
    )


class MBTI(models.Model):
    type = models.CharField(
        verbose_name='MBTI 유형',
        max_length=255,
        null=True,
        blank=False
    )
    list = models.CharField(
        verbose_name='직업목록',
        max_length=255,
        null=False,
        blank=False
    )
