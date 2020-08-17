try:
    a = {1:'Taalay', 2:'Kirill', 3:'Turat', 4:'Umka'}
    b = a[5]

except KeyError:
    print('ключа нету')
else:
    print(b)
finally:
    print('а все уже')