m, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
#####

answer = 0
data = sorted(data, reverse=True)

for i in range(1, m+1):
    if i%4==0:
        answer += data[1]
    else:
        answer += data[0]

print(answer)