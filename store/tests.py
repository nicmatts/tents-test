from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from .models import Category, Subcategory, Product, Cart, Order

from .views import home, categories, category, subcategory, all_products, single_product, add_to_cart, remove_from_cart


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
        # in the context variable for view, test for 'categories' entry
        self.assertTrue('categories' in resp.context)
        # check to make sure there is at least one category in the DB
        self.assertTrue(resp.context['categories'].count > 0)


class CategoryPageTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="test3", description="test", category_image="test.jpg")

    def test_category_page(self):
        resp = self.client.get('/products/categories/test3/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['category'].pk, 3)
        self.assertEqual(resp.context['category'].name, 'test3')
        # resp2 = self.client.get('/products/categories/no-test/')
        # self.assertEqual(resp2.status_code, 404)


class SubategoryPageTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="parent", description="test", category_image="test.jpg")
        subcategory = Subcategory.objects.create(name="subcategory", description="subcategory", subcategory_image="test.jpg", parent_category=category)

    def test_category_page(self):
        resp = self.client.get('/products/categories/parent/subcategory/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['subcategory'].pk, 1)
        self.assertEqual(resp.context['subcategory'].name, 'subcategory')


class ProductsPageTest(TestCase):
    def setUp(self):
        product = Product.objects.create(
            name="product",
            description="product",
            product_image="test.jpg",
            bismarck_weekday_price=1.00,
            bismarck_weekend_price=1.00,
            bismarck_weekly_price=1.00,
            bismarck_4_week_price=1.00,
            forx_weekday_price=1.00,
            forx_weekend_price=1.00,
            forx_weekly_price=1.00,
            forx_4_week_price=1.00,
            fargo_25_weekday_price=1.00,
            fargo_25_weekend_price=1.00,
            fargo_25_weekly_price=1.00,
            fargo_25_4_week_price=1.00,
            fargo_32_weekday_price=1.00,
            fargo_32_weekend_price=1.00,
            fargo_32_weekly_price=1.00,
            fargo_32_4_week_price=1.00,
            moorhead_weekday_price=1.00,
            moorhead_weekend_price=1.00,
            moorhead_weekly_price=1.00,
            moorhead_4_week_price=1.00,
        )

        self.user = User.objects.create_user(
            username="Name", email="test@test.com", password="password"
        )

    def test_products(self):
        resp = self.client.get('/products/all/')
        # make sure page loads
        self.assertEqual(resp.status_code, 200)
        # in the context variable for view, test for 'categories' entry
        self.assertTrue('products' in resp.context)
        # check to make sure there is at least one category in the DB
        self.assertTrue(resp.context['products'].count > 0)

    def test_product_page(self):
        resp = self.client.get('/products/product/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['product'].pk, 3)
        self.assertEqual(resp.context['product'].name, 'product')

    def test_cart(self):
        resp = self.client.get('/products/cart/')
        self.assertEqual(resp.status_code, 302)


    def test_add_to_cart(self):
        self.logged_in = self.client.login(username="Name", password="password")
        self.assertTrue(self.logged_in)
        resp = self.client.get('/products/add/1/')
        resp = self.client.get('/products/cart/')
        self.assertEqual(resp.context['count'], 1)
        self.assertEqual(resp.context['cart'].get().quantity, 1)
