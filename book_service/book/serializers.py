# -*- coding: utf-8 -*-
'''
Модуль содержит классы сериализации данных модели Книга
'''
from rest_framework import serializers
from book_service.book.models import Book

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class GetBookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=500)
    class Meta:
        model = Book
        fields = ('title', )

class UpdateBookSerializer(CreateBookSerializer):
    title = serializers.CharField(max_length=500, read_only=True)
    class Meta:
        model = Book
        fields = '__all__'