import tempfile
import os

from PIL import Image

from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from aquarium.models import Aquarium
from core import models


from rest_framework.test import APIClient
from rest_framework import status


AQUARIUM_URL = reverse('aquarium:aquarium-list')

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

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'nick@nick.nick',
            'password'
        )
        self.client.force_authenticate(self.user)

    def test_aquarium_returns_namestring(self):
        """Test creating a new aquarium with a sample user is successful
            Also test that namestring works."""
        sample_use = sample_user()
        aquarium = sample_aquarium(user=sample_use)

        self.assertEqual(str(aquarium), aquarium.name)

    def test_aquarium_returns_volume_calc(self):
        """Test creating a new user with an email is successful"""
        payload = {
            'name': 'My Sample Aq 2',
            'water_type': 'Freshish',
            'volume_liter': 50.0
        }

        defaults_payload = {
            'length_cm': 10,
            'width_cm': 10,
            'height_cm':10,
            'description': 'My aquarium description.',
            'is_planted': False
        }

        payload.update(defaults_payload)

        res = self.client.post(AQUARIUM_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        aquarium = Aquarium.objects.get(id=res.data['id'])

        self.assertEqual(aquarium.calculated_volume(), 1)
        # Returns true if password is correct

    def test_aquarium_returns_volume_liter(self):
        """Test that the aquarium returns the vol_liter instead of calc vol 
            if calc vol is 0"""
        payload = {
            'name': 'My Sample Aq 2',
            'water_type': 'Freshish',
            'volume_liter': 50.0
        }

        defaults_payload = {
            'length_cm': 10,
            'width_cm': 0,
            'height_cm':10,
            'description': 'My aquarium description.',
            'is_planted': False
        }

        payload.update(defaults_payload)

        res = self.client.post(AQUARIUM_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        aquarium = Aquarium.objects.get(id=res.data['id'])

        self.assertEqual(aquarium.calculated_volume(), 50)
# ENDFILE
