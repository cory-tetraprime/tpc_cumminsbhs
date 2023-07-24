#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cummins_main.settings.dev")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cummins_main.settings.production")
    # Needs to be here for manage.py functions

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
