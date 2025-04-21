from rest_framework import viewsets
from ..serializers.publication_serializers import PublicationListSerializers,PublicationRetrieveSerializers,PublicationWriteSerializers
from ..models import Publication
from ..utilities.pagination import MyPagenumberPagination

class publicationViewsets(viewsets.ModelViewSet):
    serializer_class = PublicationListSerializers
    queryset = Publication.objects.all().order_by('-id')
    pagination_class = MyPagenumberPagination


def get_queryset(self):
    queryset = super().get_queryset()
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return PublicationWriteSerializers
    elif self.action == 'retrieve':
        return PublicationRetrieveSerializers
    return super().get_serializer_class()
