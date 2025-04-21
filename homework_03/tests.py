import unittest
from unittest.mock import patch

from .tasks import convert_case, is_valid_date, is_prime, input_users


class TestConvertCase(unittest.TestCase):
    def test_snake_to_camel(self):
        self.assertEqual(convert_case('otus_course'), 'OtusCourse')
        self.assertEqual(convert_case('python_is_the_best'), 'PythonIsTheBest')

    def test_camel_to_snake(self):
        self.assertEqual(convert_case('OtusCourse'), 'otus_course')
        self.assertEqual(convert_case('PythonIsTheBest'), 'python_is_the_best')

    def test_force_snake(self):
        self.assertEqual(convert_case('OtusCourse', 'snake'), 'otus_course')
        self.assertEqual(convert_case('PythonIsTheBest', 'snake'), 'python_is_the_best')

    def test_force_camel(self):
        self.assertEqual(convert_case('otus_course', 'camel'), 'OtusCourse')
        self.assertEqual(convert_case('python_is_the_best', 'camel'), 'PythonIsTheBest')

    def test_edge_cases(self):
        self.assertEqual(convert_case(''), '')
        self.assertEqual(convert_case('A'), 'a')
        self.assertEqual(convert_case('a'), 'a')
        self.assertEqual(convert_case('A_', 'snake'), 'a')
        self.assertEqual(convert_case('a_', 'snake'), 'a')
        self.assertEqual(convert_case('_A', 'camel'), 'A')
        self.assertEqual(convert_case('_a', 'camel'), 'A')


class TestIsValidDate(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(is_valid_date('01.01.2000'))
        self.assertTrue(is_valid_date('31.12.2000'))
        self.assertTrue(is_valid_date('29.02.2000'))

    def test_invalid_dates(self):
        self.assertFalse(is_valid_date('32.01.2000'))
        self.assertFalse(is_valid_date('00.01.2000'))
        self.assertFalse(is_valid_date('01.13.2000'))
        self.assertFalse(is_valid_date('01.00.2000'))
        self.assertFalse(is_valid_date('01.01.0000'))

    def test_edge_cases(self):
        self.assertFalse(is_valid_date(''))
        self.assertFalse(is_valid_date('01.01'))
        self.assertFalse(is_valid_date('01.01.2000.'))
        self.assertFalse(is_valid_date('.01.2000'))
        self.assertFalse(is_valid_date('01..2000'))
        self.assertFalse(is_valid_date('01.01.2000a'))


class TestIsPrime(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))

    def test_edge_cases(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-4))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-6))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-8))
        self.assertFalse(is_prime(-9))
        self.assertFalse(is_prime(-10))


class TestInputUsers(unittest.TestCase):
    @patch('builtins.input', side_effect=['John', 'Doe', '25', '00000001', ''])
    def test_valid_user(self, mock_input):
        users = input_users()
        self.assertEqual(users, {'00000001': ('John', 'Doe', 25)})

    @patch('builtins.input', side_effect=['John', 'Doe', '17', '00000001', ''])
    def test_invalid_age(self, mock_input):
        users = input_users()
        self.assertEqual(users, {})

    @patch('builtins.input', side_effect=['John', 'Doe', '25', 'abc', ''])
    def test_invalid_id(self, mock_input):
        users = input_users()
        self.assertEqual(users, {})

    @patch('builtins.input', side_effect=['John', 'Doe', '25', '00000001', 'John', 'Doe', '25', '00000001', ''])
    def test_duplicate_id(self, mock_input):
        users = input_users()
        self.assertEqual(users, {'00000001': ('John', 'Doe', 25)})

    @patch('builtins.input', side_effect=['John', '', 'John', 'Doe', '25', '00000002', ''])
    def test_empty_surname(self, mock_input):
        users = input_users()
        self.assertEqual(users, {'00000002': ('John', 'Doe', 25)})

    @patch('builtins.input', side_effect=['John', 'Doe', '25', '00000001', 'John', 'Doe', '25', '00000002', ''])
    def test_two_valid_users(self, mock_input):
        users = input_users()
        self.assertEqual(users, {'00000001': ('John', 'Doe', 25), '00000002': ('John', 'Doe', 25)})


if __name__ == '__main__':
    unittest.main()
