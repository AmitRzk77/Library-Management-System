from rest_framework import serializers
from ..models  import Publication


class PublicationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
    
class PublicationRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class PublicationWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'