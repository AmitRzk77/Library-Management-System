from rest_framework import viewsets
from ..serializers.reviews_serializers import ReviewListSerializers,ReviewRetrieveSerializers,ReviewWriteSerializers
from ..models import Review
from ..utilities.pagination import MyPagenumberPagination

class reviewsViewsets(viewsets.ModelViewSet):
    serializer_class = ReviewListSerializers
    queryset = Review.objects.all().order_by('-id')
    pagination_class = MyPagenumberPagination


def get_queryset(self):
    queryset = super().get_queryset()
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return ReviewWriteSerializers
    elif self.action == 'retrieve':
        return ReviewRetrieveSerializers
    return super().get_serializer_class()
