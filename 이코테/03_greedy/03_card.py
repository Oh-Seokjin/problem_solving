# n, m = 3, 3
# cards = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
#####
n, m = 2, 4
cards = [[7, 3, 1, 8], [3, 3, 3, 4]]

min_values = []

for i in range(n):
    min_values.append(min(cards[i]))

print(max(min_values))