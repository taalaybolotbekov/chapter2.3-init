try:
    a = input('введите первое число: ')
    b = input('введите второе число: ')
    result = int(a) / int(b)
except ValueError:
    print('haaaaaaai keltiresinda keltiresin')
except ZeroDivisionError:
    print('На ноль делить нельзя ')
else:
    print('Результат делителя: ', result)
finally:
    print('Все данные введены правильно и короче 100% ')