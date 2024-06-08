from rest_framework import serializers
from .models import Book, Author, Genre, Login

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class meta:
        model=Login
        fields='__all__'
