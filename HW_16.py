rows = (input('Введите пожалуйста высоту фигуры в символах >>> * : '))
len_rows = len(rows)
while True:                     # Если пользователь ввел не правильно символ, запрос на ввод повторится
    if rows != len_rows * '*':
        rows = (input('Введите пожалуйста высоту фигуры в символах >>> * : '))
        len_rows = len(rows)
    else:
        break
rows = len(rows)
cols = 2 * rows
if rows % 2 == 0:
    print('Вы ввели нечетное количество символов. В следсвие этого фигура не является полной:')
else:
    print()
for i in range(rows):
    for j in range(cols):
        if j == rows//2 or i <= rows//2 and rows//2 - i <= j <= (rows//2) + i or i > rows//2 and i == j + rows//2 or \
                rows % 2 != 0 and i > rows//2 and i == rows - j + (rows//2 - 1) or \
                rows % 2 == 0 and i > rows//2 and i == rows - j + (rows//2):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()

if rows % 2 == 0:
    print('Изобрежена фигура на один символ меньше:')
    rows = rows//2
    cols = 2 * rows
    for i in range(rows):
        for j in range(cols):
            if rows - i - 1 <= j < rows + i:
                print('* ', end='')
            else:
                print('  ', end='')
        print()

    for i in range(rows-1):
        for j in range(cols-1):
            if i == j - 1 or i == cols - j - 3 or j == rows - 1:
                print('* ', end='')
            else:
                print('  ', end='')
        print()
    print('Изобрежена фигура на один символ больше:')
    rows = 2 * rows
    cols = 2 * rows
    for i in range(rows+1):
        for j in range(cols):
            if i <= rows//2 and rows - i - 1 <= j < rows + i or \
                    i > rows//2 and i == j + 1 or i > rows//2 and i == cols - j - 1 or j == rows - 1:
                print('* ', end='')
            else:
                print('  ', end='')
        print()
