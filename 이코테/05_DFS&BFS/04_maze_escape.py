n, m = 5, 6
graph = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
visited = [[0]*m for _ in range(n)]
#####

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if not graph[x][y]:
        return False
    return True

def bfs():
    global q
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

    while q:
        curr_node = q.pop(0)
        x = curr_node[0]
        y = curr_node[1]

        depth_list = []
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            depth_list.append([new_x, new_y])
        for elem in depth_list:
            new_x, new_y = elem[0], elem[1]
            if can_go(new_x, new_y):
                q.append([new_x, new_y])
                visited[new_x][new_y] = 1
                graph[new_x][new_y] = graph[x][y] + 1
                print(q)
                for row in graph:
                    print(row)
                print()


q = [[0, 0]]
visited[0][0] = 1
graph[0][0] = 1
bfs()
for row in graph:
    print(row)
