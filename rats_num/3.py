def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print("НОД двух чисел равен: ",a)

first = int(input("Введите первое число:"))
second = int(input("Введите второе число:"))
gcd(first,second)