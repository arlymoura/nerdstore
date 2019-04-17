# coding=utf-8
from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from main.models import Product

class TestProduct(TestCase):
  img = 'https://nerdstore.com.br/wp-content/uploads/2019/04/caneca-ear-lannister-02-300x300.jpg'
  def setUp(self):
      self.product = mommy.make(Product, title='Titulo1', price= 10.0, image= self.img)
      
  def test_record_creation(self):
      self.assertTrue(isinstance(self.product, Product))
      self.assertEquals(self.product.__str__(), self.product.title)
      self.assertEquals(self.product.title, self.product.title)
      self.assertEquals(self.product.price, self.product.price)
      self.assertEquals(self.product.image, self.product.image)