# -*- coding: utf-8 -*-
'''
Базовые классы для unit-тестов
'''
from django.test import TestCase
from django.db.models.fields import AutoField

class BaseTestModel(TestCase):
    '''
    Базовый тест модели
    '''
    model = None

    def test_have_model_verbose_name(self):
        '''
        Проверка наличия в классе Meta модели verbose_name
        У каждой модели должен быть human-readable наименование
        '''
        model = self.model
        if model:
            model_name = model.__name__.lower()
            verbose_name = model._meta.verbose_name
            is_equal = model_name != verbose_name
            self.assertTrue(
                is_equal,
                'Model used default class name in verbose name.')

    def test_have_model_verbose_name_plural(self):
        '''
        Проверка наличия в классе Meta модели verbose_name_plural
        У каждой модели должен быть human-readable наименование во множественном числе
        '''
        model = self.model
        if model:
            model_name = model.__name__.lower()
            verbose_name_plural = model._meta.verbose_name_plural
            is_equal = model_name != verbose_name_plural + u's'
            self.assertTrue(
                is_equal,
                'Model used default class name in verbose name.')

    def test_have_model_fields_verbose_name(self):
        '''
        Проверка наличия у каждого поля модели verbose_name
        '''
        model = self.model
        if model:
            all_fields = model._meta.fields
            for temp_field in all_fields:
                if not isinstance(temp_field, AutoField):
                    if not temp_field.name.endswith('_ptr'):
                        verbose_name = temp_field.verbose_name
                        field_name = temp_field.name.replace('_', ' ')
                        is_equal = verbose_name != field_name

                        self.assertTrue(
                            is_equal, 'Error in field: ' + field_name + str(model))