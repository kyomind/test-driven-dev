from django.test import TestCase
from django.urls import resolve

from todo.views import home_page

# Create your tests here.


class HomePageTest(TestCase):
    def test_home_page_url_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
