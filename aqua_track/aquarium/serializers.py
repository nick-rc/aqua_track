from rest_framework import serializers

from aquarium.models import Aquarium


class AquariumSerializer(serializers.ModelSerializer):
    """Serializer for aquariums"""

    is_planted = serializers.BooleanField(default=True)

    class Meta:
        model = Aquarium
        fields = ('id', 'name', 'water_type',
                    'volume_liter', 'length_cm',
                    'width_cm', 'height_cm',
                    'description', 'is_planted')
        read_only_fields = ('id',)
# TODO: Add aquarium detail serializzer when adding new components
# ENDFILE
