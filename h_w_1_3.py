a = input('Введите первое целое число >> ')
print( 'Целое представление число ', int(a))
print( 'Вещественное представление числа ', float(a))
print( 'Логическое представление числа ', bool(a))
print( 'Строковое представление числа ', a)
print()
b = input('Введите второе целое число >> ')
print('Целое + Целое = ', int(a)+int(b))
print('Целое * Целое = ', int(a)*int(b))
print('Целое + Вещественное = ', int(a)+float(b))
print('Целое * Вещественное = ', int(a)*float(b))
print('Строка + Строка = ',a+b)
print('Строка * Логическое = ', a*bool(b))
print('Строка * Целое = ', a*int(b))
print('Вещественное + Вещественное = ', float(a)+float(b))
print('Вещественное * Вещественное = ', float(a)*float(b))
print('Логическое + Логическое = ', bool(a)+bool(b))
print('Логическое * Логическое = ', bool(a)*bool(b))
print('Логическое + Целое = ', bool(a)+int(b))
print('Логическое * Целое = ', bool(a)*int(b))
print('Логическое + Вещественное = ', bool(a)+float(b))
print('Логическое * Вещественное = ', bool(a)*float(b))
