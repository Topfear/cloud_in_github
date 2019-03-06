import unittest


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.var = 1

    def test_assert_equal(self):
        self.assertEqual(1,1,msg="One is not two")

    def test_assert_False(self):
        self.assertFalse(False, msg="False is False")

    def test_assert_greater(self):
        self.assertGreater(2,1,msg="Two is more than one")

    def test_assert_less(self):
        self.assertLess(1,2)

    def test_assert_true(self):
        self.assertTrue(True)

    def test_assert_in(self):
        self.assertIn(1, [1,2,3])
