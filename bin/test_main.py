import unittest
from tests.test_message import test_message
from tests.test111 import test111
class test_main(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(test_message)
    suite.addTest(test111)
    unittest.TextTestRunner.run(suite)
