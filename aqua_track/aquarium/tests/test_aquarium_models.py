import tempfile
import os

from PIL import Image

from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from aquarium.models import Aquarium
from core import models

def sample_user(email='test@test.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

def sample_aquarium(user, **params):
    """Create a sample aquarium for testing"""
    defaults = {
        'name': 'My 40gal Breeder',
        'water_type': 'Fresh',
        'volume_liter': 151 
    }
    # Override defaults with input params.
    defaults.update(params)

    return Aquarium.objects.create(user=user, **defaults)

class AquariumModelTests(TestCase):

    def test_aquarium_returns_namestring(self):
        """Test creating a new aquarium with a sample user is successful"""
        sample_use = sample_user()
        aquarium = sample_aquarium(user=sample_use)

        self.assertEqual(str(aquarium), aquarium.name)

    def test_aquarium_returns_namestring(self):
        """Test creating a new user with an email is successful"""
        sample_use = sample_user({
            'length_cm': 10,
            'width_cm': 10,
            'height_cm':10
        })
        aquarium = sample_aquarium(user=sample_use)

        self.assertEqual(aquarium.vol_cm3, 1000)
        # Returns true if password is correct
# ENDFILE
