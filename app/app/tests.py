from django.test import TestCase

from app.calc import add

class CalcTests(TestCase):

    def test_add_numbers(self):
        res = add(5,3)
        self.assertEqual(res, 8)