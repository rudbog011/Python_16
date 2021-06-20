def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)
    return field
def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end='')
        print()
def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
                return True    
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != '*':
        return True
    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][2]:
        return True
    return False

def end_game(field):
    if win(field):
        return True
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
    return True
def new_game():
    field = create_field()
    current_symbol = 'X'

    while not end_game(field):
        print_field(field)
        print('Ходит', current_symbol)
        flag = 0
        while True:
            print('Введите номер строки и номер столбца')
            row = int(input())
            column = int(input())
            n = [1, 2, 3]
            if row not in n or column not in n:
                print('Неверный номер строки(1-3) или столбца(1-3)')
            else:
                break

        field[row - 1][column - 1] = current_symbol

        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'
    print_field(field)
    if current_symbol == 'X':
        print('Ура! Победил: O')
    else:
        print('Ура! Победил: X')
    print('Сыграем ещё? (Да/Нет)')
    answer = input()
    if answer == 'Да':
        new_game()
new_game()