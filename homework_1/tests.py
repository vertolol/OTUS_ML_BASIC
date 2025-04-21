import unittest

from .tasks import reverse_middle_digits, count_weekends, can_break_chocolate, int_to_roman, \
    is_float_with_sign


class TestTasks(unittest.TestCase):
    def test_reverse_middle_digits(self):
        self.assertEqual(reverse_middle_digits(23456), 25436)
        self.assertEqual(reverse_middle_digits(30789), 38709)
        self.assertEqual(reverse_middle_digits(12345), 14325)
        self.assertEqual(reverse_middle_digits(98765), 96785)
        self.assertEqual(reverse_middle_digits(54321), 52341)

    def test_count_weekends(self):
        self.assertEqual(count_weekends(4), 0)
        self.assertEqual(count_weekends(6), 1)
        self.assertEqual(count_weekends(14), 4)
        self.assertEqual(count_weekends(0), 0)
        self.assertEqual(count_weekends(1), 0)
        self.assertEqual(count_weekends(7), 2)
        self.assertEqual(count_weekends(100), 28)

    def test_can_break_chocolate(self):
        self.assertTrue(can_break_chocolate(2, 2, 4))
        self.assertTrue(can_break_chocolate(3, 3, 9))
        self.assertTrue(can_break_chocolate(4, 4, 16))
        self.assertFalse(can_break_chocolate(2, 2, 5))
        self.assertFalse(can_break_chocolate(3, 3, 10))
        self.assertFalse(can_break_chocolate(4, 4, 17))
        self.assertTrue(can_break_chocolate(2, 3, 6))
        self.assertTrue(can_break_chocolate(3, 2, 6))
        self.assertFalse(can_break_chocolate(2, 3, 7))
        self.assertFalse(can_break_chocolate(3, 2, 7))

    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(58), "LVIII")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")
        self.assertEqual(int_to_roman(0), "")
        self.assertEqual(int_to_roman(-1), "")

    def test_is_float_with_sign(self):
        self.assertTrue(is_float_with_sign("1"))
        self.assertTrue(is_float_with_sign("1.0"))
        self.assertTrue(is_float_with_sign(".1"))
        self.assertTrue(is_float_with_sign("-1"))
        self.assertTrue(is_float_with_sign("-1.0"))
        self.assertTrue(is_float_with_sign("-.1"))

        self.assertFalse(is_float_with_sign(""))
        self.assertFalse(is_float_with_sign("-"))
        self.assertFalse(is_float_with_sign("+"))
        self.assertFalse(is_float_with_sign("1."))
        self.assertFalse(is_float_with_sign("."))
        self.assertFalse(is_float_with_sign("1.0.0"))
        self.assertFalse(is_float_with_sign("1.0."))
        self.assertFalse(is_float_with_sign(".0."))
        self.assertFalse(is_float_with_sign("-1."))
        self.assertFalse(is_float_with_sign("-."))
        self.assertFalse(is_float_with_sign("-1.0."))
        self.assertFalse(is_float_with_sign("-.0."))


if __name__ == '__main__':
    unittest.main()
