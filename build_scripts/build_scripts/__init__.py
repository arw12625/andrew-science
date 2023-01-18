import os

__version__ = '0.1.0'

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(PROJECT_DIR, os.pardir, os.pardir)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
SITE_DIR = os.path.join(BASE_DIR, "site")