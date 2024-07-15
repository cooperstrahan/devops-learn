import unittest
from arithmetic import add, subtract, multiply, divide

class TestArithmeticFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(0, 5), 0)
        self.assertIsNone(divide(10, 0))  # Test division by zero

if __name__ == '__main__':
    unittest.main()