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
    title = models.CharField(max_length=500, verbose_name=u'Title', primary_key=True)
    page_count = models.PositiveIntegerField(verbose_name=u'Page count')
    publish_date = models.DateTimeField(verbose_name=u'Date of publication')
    author = models.CharField(max_length=700, verbose_name=u'Author')

    class Meta:
        verbose_name = u'Книга'
        verbose_name_plural = u'Книги'