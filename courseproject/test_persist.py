import unittest

class PersistDataTest(unittest.TestCase):
    def test_first_test(self):
        self.assertEqual(3,3)
    def test_second_test(self):
        self.assertTrue("PYTHON".isupper())


if __name__=="__main__":
    unittest.main()