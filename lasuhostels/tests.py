from django.test import TestCase
from django.test.client import Client
# Create your tests here.

class submit(TestCase):
    c = Client('/submit')
    code = c.get('/submit')
    assert(c==200)