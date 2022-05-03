import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings



class Aquarium(models.Model):
    """Aquarium object"""
    DEFAULT_AQ_DESCRIPTION = "My aquarium description."

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    water_type = models.CharField(max_length=255)
    volume_liter = models.DecimalField(max_digits=7, decimal_places=1)
    length_cm = models.IntegerField(default=0)
    width_cm = models.IntegerField(default=0)
    height_cm = models.IntegerField(default=0)
    description = models.CharField(max_length=255, 
                                    default=DEFAULT_AQ_DESCRIPTION)
    is_planted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def vol_cm3(self):
        
        volume = self.length_cm * self.width_cm * self.height_cm

        return int(volume)