from rest_framework import viewsets
from ..serializers.volume_serializers import VolumeListSerializers,VolumeRetrieveSerializers,VolumeWriteSerializers
from ..models import Volume
from ..utilities.pagination import MyPagenumberPagination

class volumeViewsets(viewsets.ModelViewSet):
    serializer_class = VolumeListSerializers
    queryset = Volume.objects.all().order_by('-id')
    pagination_class = MyPagenumberPagination


def get_queryset(self):
    queryset = super().get_queryset()
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return VolumeWriteSerializers
    elif self.action == 'retrieve':
        return VolumeRetrieveSerializers
    return super().get_serializer_class()
