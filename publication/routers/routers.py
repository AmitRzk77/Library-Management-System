from rest_framework.routers import DefaultRouter
from ..viewsets.publication_viewsets import publicationViewsets

router = DefaultRouter()

router.register('publication', publicationViewsets, basename = 'publicationViewsets')