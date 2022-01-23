import tempfile
import os

from PIL import Image

from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from aquarium import models


def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class AquariumModelTests(TestCase):

    def test_aquarium_returns_namestring(self):
        """Test creating a new user with an email is successful"""
        aquarium = sample_aquarium(user=self.user)

        self.assertEqual(aquarium.__str__, aquarium.name)
        # Returns true if password is correct
# ENDFILE
