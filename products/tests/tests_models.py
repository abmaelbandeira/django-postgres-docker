from django.test import TestCase
from products.models import Product

class ProductTestCase(TestCase):

    def setUp(self):
        Product.objects.create(
            description='Notebook', price=3000
        )

    def test_retorno_str(self):
        p1 = Product.objects.get(description='Notebook')
        self.assertEquals(p1.__str__(), 'Notebook')
