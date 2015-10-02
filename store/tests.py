from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .models import Category

from .views import home, categories, category


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_category_page_returns_correct_html(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


class CategoriesPageTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="test", description="test", category_image="test.jpg")
        category2 = Category.objects.create(name="test2", description="test", category_image="test.jpg")

    def test_categories(self):
        resp = self.client.get('/products/categories/')
        # make sure page loads
        self.assertEqual(resp.status_code, 200)
        # in the context variable for view, test for 'books' entry
        self.assertTrue('categories' in resp.context)
        # check to make sure there is at least one book in the DB
        self.assertTrue(resp.context['categories'].count > 0)
