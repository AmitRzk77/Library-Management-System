from rest_framework.routers import DefaultRouter
from ..viewsets.transaction_viewsets import transactionViewsets

router = DefaultRouter()

router.register('transaction', transactionViewsets, basename = 'transactionViewsets')