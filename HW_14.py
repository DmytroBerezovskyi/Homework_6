rows = (input('Введите пожалуйста высоту фигуры в символах >>> * : '))
len_rows = len(rows)
while True:                     # Если пользователь ввел не правильно символ, запрос на ввод повторится
    if rows != len_rows * '*':
        rows = (input('Введите пожалуйста высоту фигуры в символах >>> * : '))
        len_rows = len(rows)
    else:
        break
rows = len(rows)                # Подсчёт количества символов введеных пользователем
cols = 2 * rows
for i in range(rows):
    for j in range(cols):
        if rows - i - 1 <= j < rows + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()