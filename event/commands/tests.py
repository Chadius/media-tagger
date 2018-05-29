from unittest import TestCase
from unittest.mock import MagicMock

class Demo(TestCase):
    def setUp(self):
        pass

    def test_hello(self):
        self.assertEqual(2+2, 4)
