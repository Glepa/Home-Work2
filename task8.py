a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a, b)
temp = b
b = a
a = temp
print(a, b)
# а можно так (честно, подсмотрел как реализуют swap на python)
a, b = b ,a
print(a, b)