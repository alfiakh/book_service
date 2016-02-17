# -*- coding: utf-8 -*-
'''
Модуль с базовой моделью книги
'''
from django.db import models
from book_service.models import BaseModel

class Book(BaseModel):
    '''
    Модель книги
    '''
    title = models.CharField(max_length=500, verbose_name=u'Наименование', primary_key=True)
    page_count = models.PositiveIntegerField(verbose_name=u'Количество страниц')
    publish_date = models.DateTimeField(verbose_name=u'Дата публикации')
    author = models.CharField(max_length=700, verbose_name=u'Автор')

    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'