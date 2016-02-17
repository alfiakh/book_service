#!/usr/bin/env python
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_service.settings")

    from django.core.management import execute_from_command_line

    # Грязный хак по прогону миграций
    django.setup()
    from django.core.management import call_command
    from book_service.settings import DATABASES
    if DATABASES['default']['NAME'] == ':memory:':
        a = call_command('migrate')

    execute_from_command_line(sys.argv)


