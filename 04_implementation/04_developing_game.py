n, m = 4, 4
ocean = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
x, y, direction = 1, 1, 0
#####

def turn_left():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

board = [[0 for _ in range(m)] for _ in range(n)]
board[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if board[nx][ny] == 0 and ocean[nx][ny] == 0:
        x = nx
        y = ny
        board[nx][ny] = 1
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if ocean[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(cnt)