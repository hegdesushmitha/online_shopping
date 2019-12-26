import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","shopping.settings")

import django
django.setup()

from faker import Faker
from myapp.models import *
import random

f=faker()
