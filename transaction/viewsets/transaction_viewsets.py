from rest_framework import viewsets
from ..serializers.transaction_serializers import TransactionListSerializers,TransactionRetrieveSerializers,TransactionWriteSerializers
from ..models import Transaction
from ..utilities.pagination import MyPagenumberPagination

class transactionViewsets(viewsets.ModelViewSet):
    serializer_class = TransactionListSerializers
    queryset = Transaction.objects.all().order_by('-id')
    pagination_class = MyPagenumberPagination


def get_queryset(self):
    queryset = super().get_queryset()
    return queryset

def get_serializer_class(self):
    if self.action in ['create', 'update', 'partial_update']:
        return TransactionWriteSerializers
    elif self.action == 'retrieve':
        return TransactionRetrieveSerializers
    return super().get_serializer_class()
