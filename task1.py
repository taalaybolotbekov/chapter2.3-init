try:
    a = int(input('введите первое число '))
    b = int(input('введите второе число '))
    c = a / b

except ValueError:
    print('Введите число а не букву')
else:
    print(c)
finally:
    print('все данные правильны')