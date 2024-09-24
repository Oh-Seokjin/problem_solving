n=5
orders = ["R", "R", "R", "U", "D", "D"]
#####

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
directions = ["R", "L", "U", "D"]

curr_x = 1
curr_y = 1

for order in orders:
    for i in range(len(directions)):
        if order == directions[i]:
            temp_x = curr_x + dx[i]
            temp_y = curr_y + dy[i]
    if temp_x <1 or temp_y < 1 or temp_x > n or temp_y > n:
        continue
    curr_x = temp_x
    curr_y = temp_y

print(curr_x, curr_y)