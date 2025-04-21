from rest_framework import serializers
from ..models  import Book
from genre.models import Genre
from author.models import Author
from volume.models import Volume
from publication.models import Publication
class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name'] 
        ref_name = 'genre_book'

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class VolumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['id', 'name']

class PublicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'name']







class BookListSerializers(serializers.ModelSerializer):
    genre = GenreSerializers(read_only =True)
    author  = AuthorSerializers(read_only =  True)
    volume  = VolumeSerializers(read_only =  True)
    volume  = PublicationSerializers(read_only =  True)
    class Meta:
        model = Book
        
        fields = '__all__'

    
class BookRetrieveSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'


class BookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    