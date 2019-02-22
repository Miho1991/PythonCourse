



while True:
    n = input(' Введите порядковый номер числа Фибоначчи>>> ')
    if n.isdigit():
        break;
    else:
        print('Формат ввода не правильный! Введите порядковый номер числв ряда Фибоначчи!')

f1 = 0
f2 = 1
fn = 0
if int(n)==0:
    fn=0
elif int(n)==1:
    fn=1
else:
    for i in range (int(n)-1):
        fn = f1+f2
        f1 = f2
        f2 = fn
print ('Число [{}] ряда Чисел Фибоначчи - {}'.format(n,fn))
