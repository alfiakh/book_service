# -*- coding: utf-8 -*-
from book_service.unit_tests.base_unit_tests import BaseTestModel

from book_service.book.models import Book

class TestModelBook(BaseTestModel):
    model = Book
