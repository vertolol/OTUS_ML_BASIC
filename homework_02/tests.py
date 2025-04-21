import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from .tasks import sum_digits_until_one_digit, find_row_with_seats, rle_encode, caesar_cipher, create_grade_sheet, \
    print_grade_sheet


class TestTasks(unittest.TestCase):
    def test_sum_digits_until_one_digit(self):
        self.assertEqual(sum_digits_until_one_digit(1), 1)
        self.assertEqual(sum_digits_until_one_digit(10), 1)
        self.assertEqual(sum_digits_until_one_digit(100), 1)
        self.assertEqual(sum_digits_until_one_digit(123), 6)
        self.assertEqual(sum_digits_until_one_digit(999), 9)
        self.assertEqual(sum_digits_until_one_digit(123456789), 9)
        self.assertEqual(sum_digits_until_one_digit(0), 0)
        self.assertEqual(sum_digits_until_one_digit(-1), 1)
        self.assertEqual(sum_digits_until_one_digit(-10), 1)
        self.assertEqual(sum_digits_until_one_digit(-100), 1)
        self.assertEqual(sum_digits_until_one_digit(-123), 6)
        self.assertEqual(sum_digits_until_one_digit(-999), 9)
        self.assertEqual(sum_digits_until_one_digit(-123456789), 9)

    def test_find_row_with_seats(self):
        self.assertEqual(find_row_with_seats([[0,1,1,0], [1,0,0,0], [0,1,0,0]], 2), 1)
        self.assertEqual(find_row_with_seats([[0,1,1,0], [1,0,1,0], [1,1,0,1]], 2), False)
        self.assertEqual(find_row_with_seats([[0,0,0], [0,0,0]], 3), 0)
        self.assertEqual(find_row_with_seats([[1,1,1], [0,0,0]], 3), 1)
        self.assertEqual(find_row_with_seats([[1,1], [1,1]], 1), False)
        self.assertEqual(find_row_with_seats([[0]], 1), 0)
        self.assertEqual(find_row_with_seats([[1]], 1), False)
        self.assertEqual(find_row_with_seats([], 1), False)
        self.assertEqual(find_row_with_seats([[0, 0, 1, 0], [0, 0]], 2), 0)
        self.assertEqual(find_row_with_seats([[0, 1, 0], [0, 0]], 2), 1)

    def test_rle_encode(self):
        self.assertEqual(rle_encode("aaabbbbccccc"), "3a4b5c")
        self.assertEqual(rle_encode("asssdddsssddd"), "1a3s3d3s3d")
        self.assertEqual(rle_encode("abcba"), "1a1b1c1b1a")
        self.assertEqual(rle_encode(""), "")
        self.assertEqual(rle_encode("a"), "1a")
        self.assertEqual(rle_encode("bbbbbbbbbb"), "10b")
        self.assertEqual(rle_encode("ababababa"), "1a1b1a1b1a1b1a1b1a")
        self.assertEqual(rle_encode("cccccaaaaabb"), "5c5a2b")

    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("Dog", 2), "Fqi")
        self.assertEqual(caesar_cipher("Zak zak", 1), "Abl abl")
        self.assertEqual(caesar_cipher("Python is the BEST", 2), "Ravjqp ku vjg DGUV")
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesar_cipher("", 5), "")
        self.assertEqual(caesar_cipher("abc xyz ABC XYZ", 3), "def abc DEF ABC")
        self.assertEqual(caesar_cipher("Shift by zero", 0), "Shift by zero")
        self.assertEqual(caesar_cipher("Negative shift", -1), "Mdfzshud rghes")
        self.assertEqual(caesar_cipher("WrapAroundZz", 1), "XsbqBspvoeAa")


class TestCreateGradeSheetAllGrades(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        "Математика Иванов 5",
        "Математика Иванов 4",
        "Литература Иванов 3",
        "Математика Петров 5",
        "Литература Сидоров 3",
        "Литература Петров 5",
        "Литература Иванов 4",
        "Математика Сидоров 3",
        "Математика Петров 5",
        ""
    ])
    def test_create_grade_sheet_all_grades(self, mock_input):
        expected = {
            'Математика': {
                'Иванов': ['5', '4'],
                'Петров': ['5', '5'],
                'Сидоров': ['3']
            },
            'Литература': {
                'Иванов': ['3', '4'],
                'Сидоров': ['3'],
                'Петров': ['5']
            }
        }

        result = create_grade_sheet()
        self.assertEqual(result, expected)

    def test_print_grade_sheet_all_grades(self):
        grade_sheet = {
            'Математика': {
                'Иванов': ['5', '4'],
                'Петров': ['5', '5'],
                'Сидоров': ['3']
            },
            'Литература': {
                'Иванов': ['3', '4'],
                'Сидоров': ['3'],
                'Петров': ['5']
            }
        }

        expected_output = (
            "Математика\n"
            "Иванов 5 4\n"
            "Петров 5 5\n"
            "Сидоров 3\n"
            "Литература\n"
            "Иванов 3 4\n"
            "Сидоров 3\n"
            "Петров 5\n"
        )

        captured_output = StringIO()
        with redirect_stdout(captured_output):
            print_grade_sheet(grade_sheet)

        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
