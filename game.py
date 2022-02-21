field = [['-'] * 3 for i in range(3)]
count = 0

def print_field(a):
    print('  0 1 2', '\n0', *a[0],'\n1', *a[1], '\n2', *a[2])

def next_turn(a):
    global count

    while True:
        if count % 2 == 0:
            turn = list(input("Введите координаты для х:\n"))
        else:
            turn = list(input("Введите координаты для 0:\n"))

        if len(turn) != 2:
            print("Можно вводить только две координаты")
            continue

        if turn[0].isdigit() and turn[1].isdigit():
            x = int(turn[0])
            y = int(turn[1])
        else:
            print("Можно вводить только цифры")
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Координаты должны быть от 0 до 2")
            continue

        if a[x][y] != '-':
            print("Ячейка уже занята")
            continue

        if count % 2 == 0:
            a[x][y] = 'x'
        else:
            a[x][y] = '0'

        count += 1
        return count

def win_check():
    win = (((0, 0), (0, 1), (0, 2)),
           ((1, 0), (1, 1), (1, 2)),
           ((2, 0), (2, 1), (2, 2)),
           ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)),
           ((0, 2), (1, 2), (2, 2)),
           ((0, 0), (1, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)))

    for i in win:
        check_coord = []

        for j in i:
            check_coord.append(field[j[0]][j[1]])

        if check_coord[0] == check_coord[1] == check_coord[2] != '-':
            print(f"ПОБЕДИЛИ {check_coord[0]}")
            return True

    return False


while True:
    print_field(field)
    next_turn(field)
    if win_check():
        break
    if count == 9:
        print("НИЧЬЯ")
        break
