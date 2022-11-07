#Крестики нолики
field = [[" "] * 3 for i in range(3)]
def show(l):
    print(f"  | 1 | 2 | 3 |")
    print("----------------")
    for i in range(3):
        print(f"{i+1} | {field [i] [0]} | {field [i] [1]} | {field [i] [2]} |")
        print("----------------")
def ask():
    while True:
        x = int(input('введите номер строки вашего хода '))-1
        y = int(input('введите номер столбца вашего хода '))-1

        if field [x][y] != " ":
            print ('поле занято, введите координаты еще раз')
            continue
        else:
            break
    return x, y
def win_X():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["X", "X", "X"]:
            return True
    for i in range (3):
        symbols = []
        for j in range (3):
            symbols.append(field[j][i])
        if symbols == ['X','X','X']:
            return True
    symbols = []
    for i in range (3):
        symbols.append(field[i][i])
        if symbols == ["X", "X", "X"]:
            return True
    symbols = []
    for i in range (3):
        symbols.append(field[i][2-i])
        if symbols == ["X", "X", "X"]:
            return True
def win_0():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["0", "0", "0"]:
            return True
    for i in range (3):
        symbols = []
        for j in range (3):
            symbols.append(field[j][i])
        if symbols == ["0","0","0"]:
            return True
    symbols = []
    for i in range (3):
        symbols.append(field[i][i])
        if symbols == ["0", "0", "0"]:
            return True
    symbols = []
    for i in range (3):
        symbols.append(field[i][2-i])
        if symbols == ["0", "0", "0"]:
            return True
num = 0
while True:
    num +=1
    show(field)
    if num % 2 ==1:
        print('ходит крестик')
    else:
        print('ходит нолик')
    x, y = ask()
    if num % 2 == 1:
        field [x][y] = "X"
    else:
        field [x][y] = "0"
    if num == 9:
        print ('ничья!')
        show(field)
        break
    if win_X():
        print("The END - Победил крестик!!!")
        break
    if win_0():
        print("The END - Победил нолик!!!")
        break


