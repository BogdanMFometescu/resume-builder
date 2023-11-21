"""
WSGI config for resume_builder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv

from django.core.wsgi import get_wsgi_application
CURRENT_DIRECTORY = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIRECTORY.parent
ENV_FILE_PATH = BASE_DIR / '.env'

dotenv.read_dotenv(str(ENV_FILE_PATH))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resume_builder.settings')

application = get_wsgi_application()
