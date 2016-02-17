# -*- coding: utf-8 -*-
'''
Модуль с базовой моделью и всеми проверками
'''

from django.db import models

class BaseModel(models.Model):
    '''
    Базовая модель
    Включает в себя проверки данных дат, строк и т.п.
    '''
    def save(self, *args, **kwargs):
        '''
        Перед сохранением проводим некоторые проверки объекта по всем полям
        '''
        for field in self.__class__._meta.fields:
            # Получаем имя поля
            field_name = getattr(field, 'attrname', None)
            if not field_name: continue

            # Получаем значение этого поля для объекта
            value = getattr(self, field_name, None)
            if value and isinstance(field, (models.CharField, models.TextField)):
                # Заменяем дублируещиеся пробелы на единичные, убираем спец символы
                new_value = ' '.join(value.split())

        super(BaseModel, self).save(*args, **kwargs)\

    class Meta:
        abstract = True
