import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
                                        BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings


# Create USER PROFILE MODEL CALLED PROFILE
# ** HELPS SEPARATE DEFAULT USER OEPRATIONS

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates a new user based on specified input"""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        """Create a superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
# ENDFILE
