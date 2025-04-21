import math
import datetime
from typing import Optional, Dict, Tuple


def convert_case(s: str, force: Optional[str] = None) -> str:
    """
    Преобразует строку из формата снейк_кейс в формат КэмелКейс и наоборот.

    Аргументы:
    s -- входная строка
    force -- необязательный аргумент, который может быть 'snake' или 'camel'.
    Если указан, функция будет принудительно возвращать строку в указанном формате.

    Возвращает:
    Преобразованную строку.

    Если 'force' равно 'snake', функция преобразует строку в формат снейк_кейс.
    Если 'force' равно 'camel', функция преобразует строку в формат КэмелКейс.
    Если 'force' не указан, функция определяет формат входной строки и преобразует ее в противоположный формат.
    """

    def snake_to_camel(s: str) -> str:
        return ''.join([i.capitalize() for i in s.split('_')])

    def camel_to_snake(s: str) -> str:
        return ''.join(['_' + i.lower() if i.isupper() else i for i in s]).lstrip('_').rstrip('_')

    if force == 'snake':
        return camel_to_snake(s)
    elif force == 'camel':
        return snake_to_camel(s)
    else:
        if '_' in s:
            return snake_to_camel(s)
        else:
            return camel_to_snake(s)


def is_valid_date(date_str: str) -> bool:
    """
    Проверяет, является ли строка валидной датой в формате 'дд.мм.гггг'.

    Возвращает True, если дата корректна, иначе False.
    """

    try:
        day, month, year = map(int, date_str.split('.'))
        datetime.date(year, month, day)
        return True
    except (ValueError, TypeError):
        return False


def is_prime(n: int) -> bool:
    """
    Проверяет, является ли число простым.

    Возвращает True, если число простое, иначе False.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def input_users() -> Dict[str, Tuple[str, str, int]]:
    """
    Функция для ввода информации о пользователях.

    Возвращает словарь, где ключами являются ID пользователей,
    а значениями - кортежи с именем, фамилией и возрастом пользователя.

    Ввод информации о пользователях осуществляется в цикле, пока не будет введена пустая строка вместо имени.
    При вводе информации о пользователе проверяются следующие условия:
    - Имя и фамилия должны содержать только буквы.
    - Возраст должен быть числом от 18 до 60.
    - ID должен быть целым числом, который будет дополнен до 8 знаков нулями слева.
    - ID должен быть уникальным для каждого пользователя.

    Если какое-либо из условий не выполняется,
    выводится сообщение об ошибке и ввод информации о пользователе повторяется.
    """
    users = {}

    while True:
        name = input("Введите имя (пустая строка для выхода): ").strip()
        if not name:
            break

        surname = input("Введите фамилию: ").strip()
        if not surname:
            print("Фамилия не может быть пустой.")
            continue

        age_str = input("Введите возраст: ").strip()
        user_id_str = input("Введите ID: ").strip()

        if not name.isalpha() or not surname.isalpha():
            print("Имя и фамилия должны содержать только буквы.")
            continue

        name = name.capitalize()
        surname = surname.capitalize()

        if not age_str.isdigit():
            print("Возраст должен быть числом.")
            continue
        age = int(age_str)
        if age < 18 or age > 60:
            print("Возраст должен быть от 18 до 60.")
            continue

        if not user_id_str.isdigit():
            print("ID должен быть целым числом.")
            continue
        user_id_int = int(user_id_str)
        user_id = f"{user_id_int:08d}"

        if user_id in users:
            print(f"Пользователь с ID {user_id} уже существует.")
            continue

        users[user_id] = (name, surname, age)

    return users


def print_users_table(users: Dict[str, Tuple[str, str, int]]) -> None:
    """
    Функция для вывода таблицы пользователей.

    Аргументы:
    users -- словарь, где ключами являются ID пользователей,
    а значениями - кортежи с именем, фамилией и возрастом пользователя.

    Если словарь пуст, выводится сообщение "Список пользователей пуст.".
    В противном случае, выводится таблица с заголовками "ID", "Имя", "Фамилия", "Возраст"
    и данными пользователей, отсортированными по ID.
    """
    if not users:
        print("Список пользователей пуст.")
        return

    headers = ["ID", "Имя", "Фамилия", "Возраст"]

    col_widths = [
        max(len(str(id_)) for id_ in users.keys()),
        max(len(user[0]) for user in users.values()),
        max(len(user[1]) for user in users.values()),
        len(headers[3])
    ]

    col_widths[0] = max(col_widths[0], len(headers[0]))
    col_widths[1] = max(col_widths[1], len(headers[1]))
    col_widths[2] = max(col_widths[2], len(headers[2]))

    row_format = (
        f"{{:<{col_widths[0]}}} | "
        f"{{:<{col_widths[1]}}} | "
        f"{{:<{col_widths[2]}}} | "
        f"{{:>{col_widths[3]}}}"
    )

    print(row_format.format(*headers))
    print("-" * (sum(col_widths) + 9))

    for user_id in sorted(users.keys()):
        name, surname, age = users[user_id]
        print(row_format.format(user_id, name, surname, age))


if __name__ == '__main__':
    print(convert_case("otus_course"))
    print(convert_case("PythonIsTheBest"))

    print(is_valid_date("29.02.2000"))  # True (високосный год)
    print(is_valid_date("29.02.2001"))  # False (не високосный)
    print(is_valid_date("31.04.1962"))  # False (апрель — 30 дней)

    print(is_prime(17))
    print(is_prime(20))
    print(is_prime(23))

    users_dict = input_users()
    print("\nВведённые пользователи:")
    print_users_table(users_dict)

