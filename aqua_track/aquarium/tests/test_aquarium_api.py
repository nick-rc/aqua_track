import tempfile
import os

from PIL import Image

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# from app import recipe

from rest_framework.test import APIClient
from rest_framework import status

from aquarium.models import Aquarium

from aquarium.serializers import AquariumSerializer #, AquariumDetailSerializer


AQUARIUM_URL = reverse('aquarium:aquarium-list')


def detail_url(aquarium_id):
    """Return he aquarium detail URL
    - INPUT = Aquarium ID int
    """
    return reverse('aquarium:aquarium-detail', args=(aquarium_id,))


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


class PublicAquariumAPITests(TestCase):
    """Test access without authentication"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_auth_required(self):
        """Test to make sure authentication is required"""
        print("Test Auth Requred")
        res = self.client.get(AQUARIUM_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateAquariumAPITests(TestCase):
    """Test access and functionality with authentication"""
    
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'nick@nick.nick',
            'password'
        )
        self.client.force_authenticate(self.user)
    
    def test_retrieve_aquariums(self):
        """Test getting a list of the aquariums available ot the user."""
        sample_aquarium(user=self.user)
        sample_aquarium(user=self.user)

        res = self.client.get(AQUARIUM_URL)

        aquariums = Aquarium.objects.all().order_by('-id')
        serializer = AquariumSerializer(aquariums, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipes_limited_to_user(self):
        """Make sure user can only see their own recipes."""
        user2 = get_user_model().objects.create_user(
            'test@false.com',
            'passsss'
        )
        sample_aquarium(user=user2)
        sample_aquarium(user=self.user)

        res = self.client.get(AQUARIUM_URL)

        aquariums = Aquarium.objects.filter(user=self.user)
        serializer = AquariumSerializer(aquariums, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)

    def test_view_aquarium_detail(self):
        """Testing viewing the aquarium detail page."""
        aquarium = sample_aquarium(user=self.user)
        url = detail_url(aquarium.id)
        res = self.client.get(url)
        serializer = AquariumSerializer(aquarium)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_aquarium_basic(self):
        """Test creating an aquarium with the basic details"""
        payload = {
            'name': 'My Sample Aq',
            'water_type': 'Freshish',
            'volume_liter': 50.0
        }

        res = self.client.post(AQUARIUM_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        aquarium = Aquarium.objects.get(id=res.data['id'])

        for key in payload.keys():
            self.assertEqual(payload[key], getattr(aquarium, key))

    def test_full_aquarium_update(self):
        """Test changing the values of aquarium data"""
        aquarium = sample_aquarium(user=self.user)

        payload = {
            'name': "New Aq Name",
            'water_type': 'Salty',
            'volume_liter': 1
        }
        url = detail_url(aquarium.id)
        self.client.put(url, payload)

        aquarium.refresh_from_db()
        self.assertEqual(aquarium.name, payload['name'])
        self.assertEqual(aquarium.water_type, payload['water_type'])
        self.assertEqual(aquarium.volume_liter, payload['volume_liter'])
# ENDFILE
