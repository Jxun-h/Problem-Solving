from sys import stdin

dp = [0 for _ in range(11)]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(int(stdin.readline().strip())):
    print(dp[int(stdin.readline().strip().rstrip())])