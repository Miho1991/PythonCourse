
def sum(a, b):
    return a + b


def div(a, b):
    return a / b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b

y = True
while y:

    operation = {
        '+': sum,
        '-': sub,
        '*': mul,
        '/': div
    }
    check = True
    while check:
        try:
            inp_operation = input('Введите тип операции {} >>> '.format(list(operation.keys()))).strip()
            first_num = float(input('Первое число >>> '))
            second_num = float(input('Второе число >>> '))
            result = None
            result = operation[inp_operation](first_num, second_num)
            check = False
        except (ZeroDivisionError, ValueError, KeyError) as e:
            print('Ощибка операции', e)
        except Exception as er:
            print('New Exception',er)

    if result is not None:
        print('Результат: {} {} {} = {}'.format(first_num, inp_operation, second_num, round(result,2)))
        print()

    try:
        inp = input('Желаете продолжить? [n - Выход]')
        if inp == 'n':
            y = False
    except Ellipsis as e:
        print ('Ошибка ', e)