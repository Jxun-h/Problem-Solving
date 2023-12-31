from sys import stdin

n = int(stdin.readline())
left = list(map(int, stdin.readline().split()))
right = list(map(int, stdin.readline().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):

        if right[j] < left[i]:
            dp[i][j] = max(dp[i][j + 1] + right[j], dp[i + 1][j], dp[i + 1][j + 1])

        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])


print(dp[0][0])