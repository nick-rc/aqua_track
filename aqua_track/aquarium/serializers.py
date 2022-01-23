from rest_framework import serializers

from aquarium.models import Aquarium


class AquariumSerializer(serializers.ModelSerializer):
    """Serializer for aquariums"""

    class Meta:
        model = Aquarium
        fields = ('id', 'name', 'water_type', 'wolume_liter')
        read_only_fields = ('id',)
# TODO: Add aquarium detail serializzer when adding new components
# ENDFILE
