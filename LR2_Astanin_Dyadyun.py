##Задание 1
#пункт 1
a = int(input('Первое число'))
b = int(input('Второе число'))
c = int(input('Третье число'))
if b>= a <=c:
    print(a)
elif a >= b <= c:
    print(b)
elif a >= c <=b:
    print(c)
#пункт 2
a = int(input('Первое число'))
b = int(input('Второе число'))
c = int(input('Третье число'))
if 1<= a <=50:
    print(a);
if 1 <= b <= 50:
    print(b);
if 1 <= c <=50:
    print(c);
#пункт 3
m = float(input('Введите вещественное число m: '))

for x in range(1, 11):
    print(x*m)
#пункт 4
g = 0
q = 0
num = float(input('Введите число: '))#чтобы закончить последовательность введите 0
while num != 0:
    g += num
    q += 1
    num = float(input('Введите число: '))
print('Сумма: ', g)
print('Количество: ', q)

##Задание 2
stroka = str(input('Введите строку'))
StrokaFuture = stroka.split()
print(sum(map(lambda x:
              x.startswith('m') + x.startswith('M'), StrokaFuture)))


##Задание 3
A = [int(x) for x in input().split()]
print(A)
print(max(A))
A.reverse()
print(A)
avg = sum(A) / len(A)
print(avg)
print([avg if x == 0 else x for x in A])



