try:
    a = ['Taalay','Kirill','Turat','Umka']
    a.pop(5)

except IndexError:
    print('индекса нету')
else:
    print(a)
finally:
    print('все')