import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def move(x, y, d):
    cnt = 0
    sx, sy = x, y
    while True:
        print(x, y, d)
        nx, ny = x+dxs[d], y+dys[d]

        if in_range(x, y):
            if sum(visited[x][y]) >= 18:
                cnt = -1
                break
        else:
            if sum(visited[nx][ny]) >= 18:
                cnt = -1
                break

        if not in_range(nx, ny):
            d = five[d]
            visited[x][y][d] += 1
            x, y = nx, ny
            cnt += 1
            continue

        if board[nx][ny] == -1:
            break

        if board[nx][ny] == 1:
            d = one[d]
            cnt += 1
        elif board[nx][ny] == 2:
            d = two[d]
            cnt += 1
        elif board[nx][ny] == 3:
            d = three[d]
            cnt += 1
        elif board[nx][ny] == 4:
            d = four[d]
            cnt += 1
        elif board[nx][ny] == 5:
            d = five[d]
            cnt += 1

        if board[nx][ny] >= 6:
            _, x, y = worm_hole_info[board[nx][ny], nx, ny]
            continue

        if (nx, ny) == (sx, sy):
            break
        visited[nx][ny][d] += 1
        x, y = nx, ny

    return cnt

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

one = {0:1, 1:3, 2:0, 3:2}
two = {0:3, 1:0, 2:1, 3:2}
three = {0:2, 1:0, 2:3, 3:1}
four = {0:1, 1:2, 2:3, 3:0}
five = {0:1, 1:0, 2:3, 3:2}

for test_case in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    # n, x, y
    worm_hole_info = {}
    worm_hole_temp = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 6:
                worm_hole_temp.append((board[i][j], i, j))
    if worm_hole_temp:
        worm_hole_temp.sort(key=lambda x: x[0])
        for i in range(0, len(worm_hole_temp), 2):
            worm_hole_info[worm_hole_temp[i]] = worm_hole_temp[i+1]
            worm_hole_info[worm_hole_temp[i+1]] = worm_hole_temp[i]
    print(worm_hole_info)
    answer = 0

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                for d in range(4):
                    visited = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
                    answer = max(answer, move(x, y, d))

    print(f"#{test_case} {answer}")