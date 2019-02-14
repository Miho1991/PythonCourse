while True:
    a = input('Введите певрое число >>> ')
    b = input('Введите второе число >>> ')

    countA = 0
    countB = 0

    if a.isalpha() or b.isalpha():
        print('Формат ввода не правильный! Попробуйте снова!')
    elif not a.isdigit() or not b.isdigit():
        for i in range(len(a)):
            if a[i].isalpha() :
                countA += 2
            elif a[i]=='.':
                countA +=1
        for i in range(len(b)):
            if b[i].isalpha():
                countB += 2
            elif b[i]=='.':
                countB +=1
        if countB > 1 or countA > 1 or countB>=len(b) or countA>=len(a):
            print('Формат ввода не правильный! Попробуйте снова!')
        else:
            break
    else:
        break

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

print('Сумма всех натуральных чисел в промежутке от {} до {} равна {}'.format(start,stop-1,sum))
