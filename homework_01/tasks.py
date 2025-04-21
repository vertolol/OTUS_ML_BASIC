def reverse_middle_digits(num: int) -> int:
    """
    Функция переставляет три центральные цифры в зеркальном порядке и сохраняет первую и последнюю цифры без изменений.

    Аргументы:
    num (int): Пятизначное число.

    Возвращает:
    int: Число с переставленными центральными цифрами.
    """
    num_str = str(num)
    first_digit = num_str[0]
    last_digit = num_str[-1]
    middle_digits = num_str[1:-1]
    reversed_middle_digits = middle_digits[::-1]
    return int(first_digit + reversed_middle_digits + last_digit)


def count_weekends(days_until_vacation: int) -> int:
    """
    Функция вычисляет количество выходных дней до отпуска.

    Аргументы:
    days_until_vacation (int): Количество дней до отпуска.

    Возвращает:
    int: Количество выходных дней до отпуска.
    """
    weekends = 0
    for day in range(1, days_until_vacation + 1):
        weekday = day % 7
        if weekday == 6 or weekday == 0:
            weekends += 1
    return weekends


def can_break_chocolate(n: int, m: int, k: int) -> bool:
    """
    Функция проверяет, можно ли разломить шоколадку размером n x m на k кусочков.

    Аргументы:
    n (int): Количество рядов в шоколадке.
    m (int): Количество колонок в шоколадке.
    k (int): Количество кусочков, на которое нужно разломить шоколадку.

    Возвращает:
    bool: True, если шоколадку можно разломить на k кусочков, False - в противном случае.
    """
    if k > n * m:
        return False
    if k == n * m:
        return True
    if k % n == 0 and k // n < m:
        return True
    if k % m == 0 and k // m < n:
        return True
    return False


def int_to_roman(num: int) -> str:
    """
    Функция преобразует целое положительное число в римское число.

    Аргументы:
    num (int): Целое положительное число.

    Возвращает:
    str: Римское число.
    """
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


def is_float_with_sign(num: str) -> bool:
    """
    Функция проверяет, является ли введенная строка положительным или отрицательным вещественным числом.

    Аргументы:
    s (str): Введенная строка.

    Возвращает:
    bool: True, если строка является положительным или отрицательным вещественным числом, False - в противном случае.
    """
    if len(num) == 0:
        return False

    if num[0] in ('-', '+'):
        num = num[1:]
        if len(num) == 0:
            return False

    if num.count('.') > 1:
        return False

    if num.isdigit():
        return True

    if num.startswith('.'):
        if len(num) == 1:
            return False
        if num[1:].isdigit():
            return True
        else:
            return False

    if num.endswith('.'):
        return False

    if num.count('.') == 1 and num.replace('.', '').isdigit():
        return True

    return False


if __name__ == "__main__":
    num = int(input("Введите пятизначное число: "))
    print("Результат: ", reverse_middle_digits(num))

    days = int(input("Введите количество дней до отпуска: "))
    print("Количество выходных дней до отпуска: ", count_weekends(days))

    n = int(input("Введите длину шоколадки (n): "))
    m = int(input("Введите ширину шоколадки (m): "))
    k = int(input("Введите размер желаемого куска (k): "))
    print(can_break_chocolate(n, m, k))

    num = int(input("Введите целое положительное число: "))
    print("Римское число: ", int_to_roman(num))

    s = input("Введите число: ")
    print(is_float_with_sign(s))
