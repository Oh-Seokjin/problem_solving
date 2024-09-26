# n, m = 2, 15
# currency = [2, 3]
#####
n, m = 3, 4
currency = [3, 5, 7]
#####

dp = [12345]*10001

dp[0] = 0
for i in range(1, m+1):
    temp = []
    for c in currency:
        if dp[i-c] != 12345:
            temp.append(dp[i-c]+1)
    print(i, temp)
    if temp:
        dp[i] = min(temp)

print(dp[:m+1])
if dp[m] == 12345:
    print(-1)
else:
    print(dp[m])