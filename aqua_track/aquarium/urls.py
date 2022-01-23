from django.urls import path, include
from rest_framework.routers import DefaultRouter

from aquarium import views


router = DefaultRouter()

router.register('aquariums', views.AquariumViewSet)

app_name = 'aquarium'

urlpatterns = [
    path('', include(router.urls)),
]