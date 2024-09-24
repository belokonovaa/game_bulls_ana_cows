import random


def generate_unique_number() -> int:
    """
    Генерирует случайное число от 101 до 999 с уникальными цифрами.
    """
    while True:
        number = random.randint(101, 999)  # Генерация случайного числа
        digits = set(str(number))  # Преобразование числа в набор цифр
        if len(digits) == 3:  # Проверка на уникальность цифр
            return number  # Возвращаем число, если цифры уникальны


def get_feedback(player_digits: list, digits: list) -> tuple:
    """
    Сравнивает введенные игроком цифры с загаданными и рассчитывает количество быков и коров.
    """
    bulls, cows = 0, 0  # Инициализация счетчиков быков и коров
    for i in range(3):
        if player_digits[i] == digits[i]:  # Проверка быков
            bulls += 1
        elif player_digits[i] in digits:  # Проверка коров
            cows += 1
    return bulls, cows  # Возвращаем количество быков и коров


# Рандомайзер загадывает число
number = generate_unique_number()
digits = [int(i) for i in str(number)]  # Преобразуем его в список цифр

# Приветствие
name = input('Как тебя зовут? ')
print(
    f'Привет, {name.title()}! Хочу с тобой сыграть в игру "Быки и коровы". '
    f'\nЕсли захочешь выйти из игры - набери 000.')

responses = []  # Список для хранения ответов игрока

while True:
    version = input('Введите 3х-значное число: ')

    # Выход из игры
    if version == '000':
        print(f'Это было число - {number}. Удачи в следующий раз!')
        break

    responses.append(version)  # Сохраняем ответ игрока
    player_digits = [int(i) for i in version]  # Преобразуем введенное число в список цифр

    # Проверка, угадал ли игрок число
    if int(version) == number:
        print(
            f'Поздравляю, {name.title()}! Это число - {number}! Ты использовал {len(responses)} попыток!')
        break

    bulls, cows = get_feedback(player_digits, digits)  # Получаем количество быков и коров

    # Формируем ответ в зависимости от количества быков и коров
    if bulls > 0 and cows > 0:
        print(f'У тебя {bulls} бык(а) и {cows} корова(ы).')
    elif bulls > 0:
        print(f'У тебя {bulls} бык(а).')
    elif cows > 0:
        print(f'У тебя {cows} корова(ы).')
    else:
        print('У тебя 0 быков и 0 коров.')

# Вывод ответов пользователя
answer = input('Хочешь посмотреть свои ответы? (да/нет) ')
if answer.lower() == 'да':
    print('Твои ответы:')
    for option in responses:  # Перебираем сохраненные ответы
        print(f'- {option}')
else:
    print('Спасибо за игру!')
