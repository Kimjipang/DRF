from rest_framework import serializers
from example.models import Book

class BookSerializer(serializers.ModelSerializer): # Python 코드를 JSON으로 바꾸어주거나 JSON을 Python 코드로 바꾸어주는 역할이 Serializer(직렬화)
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']
        
