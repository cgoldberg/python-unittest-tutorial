
import unittest

class InequalityTest(unittest.TestCase):

    def test_equal(self):
        self.assertNotEqual(1, 3-2)

    def test_not_equal(self):
        self.assertEqual(2, 3-2)

if __name__ == '__main__':
    unittest.main()
