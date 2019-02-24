def get_fibonachi(n):
	f1 = 0
	f2 = 1
	fn = 0
	n = int(n)
	if n == 0:
		fn = 0
	elif n == 1:
		fn = 1
	else:
		for i in range(n - 1):
			fn = f1 + f2
			f1 = f2
			f2 = fn
	print('Число [{}] ряда Чисел Фибоначчи - {}'.format(n, fn))

def main ():
	while True:
		n = input(' Введите порядковый номер числа Фибоначчи>>> ')
		if n.isdigit():
			break;
		else:
			print('Формат ввода не правильный! Введите порядковый номер числв ряда Фибоначчи!')
	get_fibonachi(n)

main()