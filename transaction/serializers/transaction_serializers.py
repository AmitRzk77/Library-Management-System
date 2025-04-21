from rest_framework import serializers
from ..models  import Transaction


class TransactionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    
class TransactionRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'