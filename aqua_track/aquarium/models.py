import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings


class Aquarium(models.Model):
    """Aquarium object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    water_type = models.CharField(max_length=255)
    volume_liter = models.DecimalField(max_digits=7, decimal_places=1)

    def __str__(self):
        return self.name