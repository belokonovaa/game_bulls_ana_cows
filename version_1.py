import random

# Рандомайзер загадывает число
number = random.randint(100,999)

# Преобразование загаданного числа в список цифр
digits = [int(i) for i in str(number)]

# Приветствие
name = input('Как тебя зовут? ')
print('Привет, ' + name.title() + '!' +
      '\nХочу с тобой сыграть в игру "Быки и коровы".'
      '\nЕсли захочешь выйти из игры - набери 000.')

# создание пустого списка для сохранения ответов игрока
responses = []

while True:
    # запрос 3х-значного числа у игрока и сохранение всех ответов в списке
    version = input('Введите 3х-значное число: ')
    responses.append(version)

    # Преобразование числа, введенного игроком в список цифр
    player_digits = [int(i) for i in str(version)]

    # Выход из игры
    if int(version) == 000:
        print('Это было число - ' + str(number) + '. \nУдачи в следующий раз!')
        break

    # Проверка числа, введенного игроком с загаданным числом
    # Если игрок отгадал число - вывод поздравлений в терминал
    if int(version) == int(number):
        print('Поздравляю, ' + name.title() + '!' + ' Это число - ' + str(number) + '!' )

        # Вывод на экран за сколько попыток игрок отгадал число
        if len(responses) == 1:
            print('Ты использовал 1 попытку!')
        elif 2 >= len(responses) <= 4:
            print('Ты использовал ' + str(len(responses)) + ' попытки!')
        elif len(responses) >= 5:
            print('Ты использовал ' + str(len(responses)) + ' попыток!')
        break

        # проверка 1 цифры
    elif (player_digits[0] == digits[0]) and (
            player_digits[1] not in digits) and (
            player_digits[2] not in digits):
        print('У тебя 1 бык')
    elif (player_digits[0] in digits) and (player_digits[1] not in digits) and (
            player_digits[2] not in digits):
        print("У тебя 1 корова")

        # проверка 2 цифры
    elif (player_digits[1] == digits[1]) and (
            player_digits[0] not in digits) and (
            player_digits[2] not in digits):
        print('У тебя 1 бык')
    elif (player_digits[1] in digits) and (player_digits[0] not in digits) and (
            player_digits[2] not in digits):
        print("У тебя 1 корова")

        # проверка 3 цифры
    elif (player_digits[2] == digits[2]) and (
            player_digits[0] not in digits) and (
            player_digits[1] not in digits):
        print('У тебя 1 бык')
    elif (player_digits[2] in digits) and (player_digits[0] not in digits) and (
            player_digits[1] not in digits):
        print("У тебя 1 корова")

        # проверка комбинаций по быкам
    elif (player_digits[0] == digits[0]) and (
            player_digits[1] == digits[1]) and (player_digits[2] not in digits):
        print('У тебя 2 быка')
    elif (player_digits[0] == digits[0]) and (
            player_digits[2] == digits[2]) and (player_digits[1] not in digits):
        print('У тебя 2 быка')
    elif (player_digits[1] == digits[1]) and (
            player_digits[2] == digits[2]) and (player_digits[0] not in digits):
        print('У тебя 2 быка')

        # проверка по быкам и коровам
    elif (player_digits[0] == digits[0]) and (player_digits[1] in digits) and (
            player_digits[2] not in digits):
        print('У тебя 1 бык и 1 корова')
    elif (player_digits[0] == digits[0]) and (player_digits[2] in digits) and (
            player_digits[1] not in digits):
        print('У тебя 1 бык и 1 корова')
    elif (player_digits[1] == digits[1]) and (player_digits[0] in digits) and (
            player_digits[2] not in digits):
        print('У тебя 1 бык и 1 корова')
    elif (player_digits[1] == digits[1]) and (player_digits[2] in digits) and (
            player_digits[0] not in digits):
        print('У тебя 1 бык и 1 корова')
    elif (player_digits[2] == digits[2]) and (player_digits[0] in digits) and (
            player_digits[1] not in digits):
        print('У тебя 1 бык и 1 корова')
    elif (player_digits[2] == digits[2]) and (player_digits[1] in digits) and (
            player_digits[0] not in digits):
        print('У тебя 1 бык и 1 корова')

    elif (player_digits[0] == digits[0]) and (player_digits[1] in digits) and (
            player_digits[2] in digits):
        print('У тебя 1 бык и 2 коровы')
    elif (player_digits[1] == digits[0]) and (player_digits[0] in digits) and (
            player_digits[2] in digits):
        print('У тебя 1 бык и 2 коровы')
    elif (player_digits[2] == digits[0]) and (player_digits[0] in digits) and (
            player_digits[1] in digits):
        print('У тебя 1 бык и 2 коровы')

    elif (player_digits[0] == digits[0]) and (
            player_digits[1] == digits[1]) and (player_digits[2] in digits):
        print('У тебя 2 быка и 1 корова')
    elif (player_digits[0] == digits[0]) and (
            player_digits[2] == digits[2]) and (player_digits[1] in digits):
        print('У тебя 2 быка и 1 корова')
    elif (player_digits[1] == digits[1]) and (
            player_digits[2] == digits[2]) and (player_digits[0] in digits):
        print('У тебя 2 быка и 1 корова')

    # проверка комбинаций по коровам
    elif (player_digits[0] in digits) and (player_digits[1] in digits) and (
            player_digits[2] not in digits):
        print("У тебя 2 коровы")
    elif (player_digits[0] in digits) and (player_digits[2] in digits) and (
            player_digits[1] not in digits):
        print("У тебя 2 коровы")
    elif (player_digits[1] in digits) and (player_digits[2] in digits) and (
            player_digits[0] not in digits):
        print("У тебя 2 коровы")
    elif (player_digits[0] in digits) and (player_digits[1] in digits) and (
            player_digits[2] in digits):
        print("У тебя 3 коровы")

    else:
        print('У тебя 0 быков и 0 коров')

# Вывод на экран всех ответов пользователя, если игрок ответил "да"
answer = input('Хочешь посмотреть свои ответы? (да/нет) ')
if answer.lower() == 'да':
    print('Твои ответы: ')
    for option in responses:
        print('- ' + option)

# вывод благодарности за игру, если игрок ответил "нет"
if answer.lower() == 'нет':
    print('Спасибо за игру!')




