from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from aquarium.models import Aquarium

from aquarium import serializers


class BaseAquariumAttrViewSet(viewsets.GenericViewSet,
                              mixins.ListModelMixin,
                              mixins.CreateModelMixin):
    """Base viewset for user owned aquarium attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current user"""    
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create new aquarium"""
        serializer.save(user=self.request.user)
    

class AquariumViewSet(viewsets.ModelViewSet):
    """Manage Aquarium Objects"""
    serializer_class = serializers.AquariumSerializer
    queryset = Aquarium.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def _params_to_ints(self, ):
        """Convert list of string IDs to ints"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Get the aquariums for the secufuc user"""
        queryset = self.queryset

        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        """Get serializer class for aquarium"""
        if self.action == 'retrieve':
            return serializers.AquariumSerializer
        
        return self.serializer_class

    def perform_create(self, serializer):
        """Create aquarium"""
        serializer.save(user=self.request.user)

# ENDFILE
