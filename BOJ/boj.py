r, c, m = map(int, input().split())
board = [[[]] * c for _ in range(r)]
for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    if d <= 2:
        s = s % (r*2-2)
    else:
        s = s % (c*2-2)
    board[x - 1][y - 1] = [(s, d, z)]

def fish(j):
    global board
    for i in range(r):
        if board[i][j] != []:
            fish_value = board[i][j][0][2]
            board[i][j] = []
            return fish_value
    return 0


def move():
    global board
    temp_board = [[[]] * c for _ in range(r)]

    # 움직임
    for i in range(r):
        for j in range(c):
            if board[i][j] != []:
                if board[i][j][0][1] <= 2:
                    t = vertical_fish(i, j, *board[i][j][0])
                    if temp_board[t[0]][t[1]] == []:
                        temp_board[t[0]][t[1]] = [(t[2], t[3], t[4])]
                    else:
                        temp_board[t[0]][t[1]].append((t[2], t[3], t[4]))
                else:
                    t = horizontal_fish(i, j, *board[i][j][0])
                    if temp_board[t[0]][t[1]] == []:
                        temp_board[t[0]][t[1]] = [(t[2], t[3], t[4])]
                    else:
                        temp_board[t[0]][t[1]].append((t[2], t[3], t[4]))

    # 잡아먹음
    for i in range(r):
        for j in range(c):
            if len(temp_board[i][j]) >= 2:
                temp_board[i][j] = [(max(temp_board[i][j], key=lambda x: x[2]))]

    board = temp_board


def vertical_fish(x, y, s, d, z):
    for _ in range(s):
        if d == 1 and x - 1 == -1:
            d = 2
        elif d == 2 and x + 1 == r:
            d = 1

        if d == 1:
            x -= 1
        elif d == 2:
            x += 1
    return (x, y, s, d, z)


def horizontal_fish(x, y, s, d, z):
    for _ in range(s):
        if d == 3 and y + 1 == c:
            d = 4
        elif d == 4 and y - 1 == -1:
            d = 3

        if d == 3:
            y += 1
        elif d == 4:
            y -= 1
    return (x, y, s, d, z)

answer = 0

for j in range(c):
    answer += fish(j)
    move()

print(answer)