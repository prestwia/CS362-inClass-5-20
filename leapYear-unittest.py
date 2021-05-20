import unittest
from leapYear import leapYear

l1 = leapYear()

class testPalindrome(unittest.TestCase):
    def test_true(self):
        self.assertEqual(l1.leapYear(2016), True)
        self.assertEqual(l1.leapYear(2020), True)
        self.assertEqual(l1.leapYear(1986), True)

    def test_false(self):
        self.assertEqual(l1.leapYear(2017), False)
        self.assertEqual(l1.leapYear(1927), True)
        self.assertEqual(l1.leapYear(2012), True)
        

    def test_type_error(self):
        with self.assertRaises(TypeError):
            l1.leapYear('a')
            l1.leapYear('#$@$')
            l1.leapYear(1.0)

if __name__ == '__main__':
    unittest.main()