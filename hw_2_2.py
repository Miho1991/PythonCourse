



while True:
    n = input(' Введите порядковый номер числа Фибоначчи>>> ')
    if n.isdigit():
        break;
    else:
        print('Формат ввода не правильный! Введите число!')

f1 = 0
f2 = 1

for i in range (int(n)-1):
    fn = f1+f2
    f1 = f2
    f2 = fn

print ('Число [{}] ряда Чисел Фибоначчи - {}'.format(n,fn))
