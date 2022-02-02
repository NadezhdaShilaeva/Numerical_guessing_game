from random import *

def is_valid(string, n):
    return string.isdigit() and 1 <= int(string) <= n

print('Добро пожаловать в числовую угадайку')
print('Хотите сыграть в игру? (д - да, н - нет)')

while input().lower() == 'д':
    n = int(input('Введите диапазон загадываемого числа\n'))
    num = randint(1, n)
    print('Число загадано. Попробуйте его угадать')
    count = 0
    while True:
        val = input('Введите целое число от 1 до ' + str(n) + '\n')
        if is_valid(val, n):
            val = int(val)
            count += 1
        else:
            print('А может быть все-таки введем целое число от 1 до ' + str(n) + '?')
            continue
        if val < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif val > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
    print('Количество сделанных вами попыток при угадывании числа:', count)
    print('Сыграем в игру еще раз? (д - да, н - нет)')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')