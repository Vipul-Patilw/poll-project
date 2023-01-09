from django.test import TestCase

# Create your tests here..
import datetime
from django.utils import timezone
c = timezone.now()
d = c + datetime.timedelta(minutes=5)
print(d)
