from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_stock_availabler(self):
        product = Product.objects.create(
            name='Pak Bepe',
            price=100000,
            description='Pak Bepe adalah seorang yang sangat baik dan ramah',
            stock=67,
        )
        self.assertTrue(product.is_stock_available)