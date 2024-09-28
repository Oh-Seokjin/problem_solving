n, m = 4, 5
graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
#####

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 1:
        return False
    return True

cnt = 0

def dfs(x, y):
    flag = 0
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y) and graph[new_x][new_y] == 0:
            flag = 1
            graph[new_x][new_y] = 1
            dfs(new_x, new_y)
    return flag


for x in range(n):
    for y in range(m):
        if dfs(x, y):
            cnt += 1

print(cnt)