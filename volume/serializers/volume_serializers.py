from rest_framework import serializers
from ..models  import Volume


class VolumeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'


    
class VolumeRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'


class VolumeWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'