import sys
sys.stdin = open("./test_cases/21425_+=.txt", "r")

t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]

for elem in arr:
    a, b, n = elem[0], elem[1], elem[2]
    cnt = 0
    while True:
        if a>n or b>n:
            break
        if a >= b:
            b += a
            cnt += 1
        else:
            a += b
            cnt += 1
    print(cnt)