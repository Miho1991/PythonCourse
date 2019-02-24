def print_result(text):
    return print(text)

def sum_natural_numbers(a,b):
    A = int(float(a))
    B = int(float(b))
    sum = 0
    if A < B:
        start = A
        stop = B + 1
        r = float(a)
    elif B <= A:
        start = B
        stop = A + 1
        r = float(b)
    for i in range(start, stop):
        if i < r or i < 0:
            continue
        sum += i
    print_result('Сумма всех натуральных чисел в промежутке от {} до {} равна {}'.format(start, stop - 1, sum))

def check_input(a, b):
    countA = 0
    countB = 0
    minCountA = 0
    minCountB = 0

    for i in range(len(a)):
        if a[i] == '.' and len(a) > 1:
            countA += 1
            continue
        elif a[i] == '-' and len(a) > 1:
            minCountA += 1
            continue
        elif not a[i].isdigit():
            countA += 2
    for i in range(len(b)):
        if b[i] == '.' and len(b) > 1:
            countB += 1
            continue
        elif b[i] == '-' and len(b) > 1:
            minCountB += 1
            continue
        elif not b[i].isdigit():
            countB += 2
    if countB > 1 or countA > 1 or minCountB > 1 or minCountA > 1 or minCountB >= len(b) or minCountA >= len(a):
        print_result('Формат ввода не правильный! Попробуйте снова!')
    else:
        return True

def main():
    while True:
        a = input('Введите певрое число >>> ')
        b = input('Введите второе число >>> ')
        check = check_input(a,b)
        if check:
            break
    sum_natural_numbers(a,b)

main()