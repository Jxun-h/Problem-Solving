from sys import stdin
MAX = int(1e6)

dp = [1]*(MAX+1)
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
        dp[i*j] += i
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + dp[i]

ans = []
for _ in range(int(stdin.readline())):
    ans.append(s[int(stdin.readline())])

print(*ans, sep='\n')