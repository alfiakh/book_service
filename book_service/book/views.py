# -*- coding: utf-8 -*-
'''
Модуль содержит view, обрабатывающего все запросы к сервису
'''
import json

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from book_service.book.serializers import (
    CreateBookSerializer, GetBookSerializer, UpdateBookSerializer)
from book_service.book.models import Book

class BookServiceResponse(HttpResponse):
    def __init__(self, book_data=None, service_code=200, message='', **kwargs):
        if service_code != 200 and not message:
            raise Exception(u'Message Required!')
        response_body_params = {
            'service_code': service_code,
            'message':message,
        }
        if book_data:
            response_body_params['data'] = book_data
        content = JSONRenderer().render(response_body_params)
        kwargs['content_type'] = 'application/json'
        super(BookServiceResponse, self).__init__(content, **kwargs)

def service_view(request):
    if not 'HTTP_XBOOK_DATA' in request.META:
        return BookServiceResponse(
            service_code=401,
            message='Please, specify book data!')
    book_data_json = request.META['HTTP_XBOOK_DATA']
    if request.method == 'POST':
        serialized_book = CreateBookSerializer(data=json.loads(book_data_json))
        if not serialized_book.is_valid():
            return  BookServiceResponse(
                service_code=402,
                message=serialized_book.errors)
        serialized_book.save()
        return BookServiceResponse(message=u'Book succesfully saved!')

    elif request.method == 'PUT':
        serialized_upd_data = json.loads(book_data_json)
        serialized_book = UpdateBookSerializer(data=serialized_upd_data)
        if not serialized_book.is_valid():
            return  BookServiceResponse(
                service_code=402,
                message=serialized_book.errors)
        try:
            book = Book.objects.get(title=serialized_upd_data['title'])
        except Book.DoesNotExist:
            return  BookServiceResponse(
                service_code=403,
                message=u'Book with this title doesn\'t exist')
        serialized_book.update(book, serialized_book.validated_data)
        return BookServiceResponse(message=u'Book succesfully updated!')

    elif request.method =='GET' or request.method == 'DELETE':
        serialized_title = json.loads(book_data_json)
        serialized_title = GetBookSerializer(data=serialized_title)
        if not serialized_title.is_valid():
            return  BookServiceResponse(
                service_code=402,
                message=serialized_title.errors)
        try:
            book = Book.objects.get(title=serialized_title['title'].value)
        except Book.DoesNotExist:
            return  BookServiceResponse(
                service_code=403,
                message=u'Book with this title doesn\'t exist')
        if  request.method == 'GET':
            book_data = CreateBookSerializer(book)
            return  BookServiceResponse(
                service_code=200,
                message=u'Book successfully found',
                book_data=book_data.data)
        elif request.method == 'DELETE':
            book.delete()
            return  BookServiceResponse(
                service_code=200,
                message=u'Book successfully deleted')
    return BookServiceResponse(
        service_code= 404,
        message=u'No such method for service!'
    )