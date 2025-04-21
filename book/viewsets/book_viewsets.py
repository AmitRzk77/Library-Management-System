from rest_framework import viewsets
from ..serializers.book_serializers import BookListSerializers,BookRetrieveSerializers,BookWriteSerializers
from ..models import Book
from ..utilities.pagination import MyPagenumberPagination
from rest_framework.permissions import IsAuthenticated


class bookViewsets(viewsets.ModelViewSet):
    serializer_class = BookListSerializers
    queryset = Book.objects.all().order_by('-id')
    pagination_class = MyPagenumberPagination
    permission_classes = [IsAuthenticated]


def get_queryset(self):
    queryset = super().get_queryset()  #here we can apply authorization for data
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return BookWriteSerializers
    elif self.action == 'retrieve':
        return BookRetrieveSerializers
    return super().get_serializer_class()
