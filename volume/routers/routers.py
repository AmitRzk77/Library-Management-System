from rest_framework.routers import DefaultRouter
from ..viewsets.volume_viewsets import volumeViewsets

router = DefaultRouter()

router.register('volume', volumeViewsets, basename = 'volumeViewsets')