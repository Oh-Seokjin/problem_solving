def gravity():
    global board
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                board[i].pop(j)
                board[i].append(0)

    board = [x[::-1] for x in board]

    after = [[] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if j == n - 1:
                if board[i][j] > 0:
                    after[i].append(board[i][j])
                continue

            t1, t2 = board[i][j], board[i][j + 1]

            if t1 == t2:
                if t1 + t2 > 0:
                    after[i].append(t1 * 2)
                    board[i][j] = 0
                    board[i][j + 1] = 0
            else:
                if t1 > 0:
                    after[i].append(t1)
                    board[i][j] = 0
        for j in range(n - len(after[i])):
            after[i].append(0)

    after = [x[::-1] for x in after]
    board = after

def rotate(n):
    global board
    if n == 90:
        board = list(map(list, zip(*board[::-1])))
    elif n == 180:
        board = [x[::-1] for x in board[::-1]]
    elif n == 270:
        board = [x[::-1] for x in list(map(list, zip(*board[::-1])))][::-1]

import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, d = input().split()
    n = int(n)
    board = [list(map(int, input().split())) for _ in range(n)]

    if d == "right":
        gravity()
    elif d == "left":
        rotate(180)
        gravity()
        rotate(180)
    elif d == "up":
        rotate(90)
        gravity()
        rotate(270)
    elif d == "down":
        rotate(270)
        gravity()
        rotate(90)

    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()