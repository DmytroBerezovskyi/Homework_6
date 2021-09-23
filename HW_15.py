rows = (input('Введите пожалуйста высоту фигуры в символах >>> * : '))
len_rows = len(rows)
while True:                     # Если пользователь ввел не правильно символ, запрос на ввод повторится
    if rows != len_rows * '*':
        rows = (input('Введите пожалуйста высоту фигуры в символах >>> * : '))
        len_rows = len(rows)
    else:
        break

rows = len(rows)
cols = rows
rows = rows//2                # Подсчёт количества символов введеных пользователем
for i in range(rows):
    for j in range(cols):
        if rows - i - 1 <= j < rows + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

cols = 2 * rows
for i in range(rows-1):
    for j in range(cols-1):
        if i == j - 1 or i == cols - j - 3:  
            print('* ', end='')
        else:
            print('  ', end='')
    print()



rows = rows * 2
cols = 2 * rows
for i in range(rows+1):
    for j in range(cols):
        if i <= rows//2 and rows - i - 1 <= j < rows + i or i > rows//2 and i == j + 1 or i > rows//2 and i == cols - j - 1 :
            print('* ', end='')
        else:
            print('  ', end='')
    print()
