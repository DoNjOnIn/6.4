import unittest
from main import max

class MyTestCase(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max(0,2,[2,-3,6,5,3],0),2)
