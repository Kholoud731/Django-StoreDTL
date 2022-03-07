from email.mime import image
from turtle import title
from django.test import TestCase

from ..models import Product, Category
from django.contrib.auth.models import User


class TestCategoryModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_Category_creation(self):

        data = self.data1
        self.assertTrue(isinstance(data,Category))
        self.assertTrue(str(data), 'django')

class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, created_by_id=1, title='django one', slug='django', price='30.4',image='django' )

    def test_Product_creation(self):

        data = self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertTrue(str(data), 'django one')