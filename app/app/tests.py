from django.test import TestCase
from app.calc import add,sub

class CalcTest(TestCase):

    def test_add_number(self):
        """Test two number sum together"""
        x=4
        y=5
        self.assertEqual(add(x,y),9)
    def test_subtract_number(self):
        """Test subtract two number return"""
        self.assertEqual(sub(4,8),4)
