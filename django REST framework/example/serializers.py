from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bid = validated_date.get('bid', instance.bid)
        instance.title = validated_date.get('title', instance.title)
        instance.author = validated_date.get('author', instance.author)
        instance.category = validated_date.get('category', instance.category)
        instance.pages = validated_date.get('pages', instance.pages)
        instance.price = validated_date.get('price', instance.price)
        instance.published_date = validated_date.get('published_date', instance.published_date)
        instance.description = validated_date.get('description', instance.description)
        instance.save()
        return instance
