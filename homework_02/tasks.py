from typing import Dict


def sum_digits_until_one_digit(n: int) -> int:
    """
    Функция суммирует цифры числа до тех пор, пока не останется одна цифра.

    Аргументы:
    n (int): Число, цифры которого нужно суммировать.

    Возвращает:
    int: Одна цифра, полученная в результате суммирования цифр числа.
    """
    n = abs(n)  # на случай отрицательного числа
    while n >= 10:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    return n


def find_row_with_seats(cinema: list[list[int]], tickets: int) -> int | bool:
    """
    Ищет ряд с достаточным количеством подряд идущих свободных мест.

    :param cinema: Список рядов, каждый ряд — список мест (0 — свободно, 1 — занято).
    :param tickets: Количество требуемых билетов.
    :return: Индекс ряда с подходящими местами или False, если таких нет.
    """
    for row_index, row in enumerate(cinema):
        free_count = 0
        for seat in row:
            if seat == 0:
                free_count += 1
                if free_count == tickets:
                    return row_index
            else:
                free_count = 0
    return False


def rle_encode(s: str) -> str:
    """
    Функция кодирует строку с использованием алгоритма RLE.

    Аргументы:
    s (str): Строка, которую нужно закодировать.

    Возвращает:
    str: Закодированная строка.
    """
    if not s:
        return ""

    result = []
    count = 1
    prev_char = s[0]

    for char in s[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count}{prev_char}")
            prev_char = char
            count = 1

    result.append(f"{count}{prev_char}")

    return "".join(result)


def caesar_cipher(text: str, key: int) -> str:
    """
    Функция шифрует строку с использованием алгоритма Цезаря.

    Аргументы:
    text (str): Строка, которую нужно зашифровать.
    key (int): Ключ шифрования.

    Возвращает:
    str: Зашифрованная строка.
    """
    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result.append(chr(shifted))
        elif char == ' ':
            result.append(char)
        else:
            result.append(char)

    return "".join(result)


def create_grade_sheet() -> Dict[str, Dict[str, list]]:
    """
    Функция создает таблицу успеваемости.

    Возвращает:
    dict: Словарь, где ключи - названия предметов, а значения - словари,
    где ключи - фамилии учеников, а значения - оценки.
    """
    grade_sheet = {}
    while True:
        data = input("Введите данные в формате 'название предмета' 'фамилия ученика' 'оценка': ")
        if not data:
            break
        subject, student, grade = data.split()
        if subject not in grade_sheet:
            grade_sheet[subject] = {}
        if student not in grade_sheet[subject]:
            grade_sheet[subject][student] = []
        grade_sheet[subject][student].append(grade)

    return grade_sheet


def print_grade_sheet(grade_sheet):
    """
    Функция выводит таблицу успеваемости.

    Аргументы:
    grade_sheet (dict): Словарь, где ключи - названия предметов, а значения - словари, где ключи - фамилии учеников, а значения - оценки.
    """
    for subject, students in grade_sheet.items():
        print(subject)
        for student, grade in students.items():
            print(student, *grade)


if __name__ == "__main__":
    num = int(input("Введите число: "))
    print("Результат: ", sum_digits_until_one_digit(num))

    cinema = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]
    tickets = 2
    print("Результат: ", find_row_with_seats(cinema, tickets))

    s = input("Введите строку: ")
    print("Результат: ", rle_encode(s))

    s = input("Введите строку: ")
    key = int(input("Введите ключ шифрования: "))
    print("Результат: ", caesar_cipher(s, key))

    grade_sheet = create_grade_sheet()
    print_grade_sheet(grade_sheet)
