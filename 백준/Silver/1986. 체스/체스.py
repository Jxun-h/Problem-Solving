from sys import stdin

n, m = map(int, stdin.readline().split())

q_info = list(map(int, stdin.readline().split()))
k_info = list(map(int, stdin.readline().split()))
p_info = list(map(int, stdin.readline().split()))

q_info, k_info, p_info = q_info[1:], k_info[1:], p_info[1:]

grid = [['' for _ in range(m)] for _ in range(n)]
qdy, qdx = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
kdy, kdx = [-1, 1, 2, 2, -1, 1, -2, -2], [2, 2, 1, -1, -2, -2, -1, 1]

mxln = max(n, m)

chk = [[0 for _ in range(m)] for _ in range(n)]

for i in range(len(q_info)):
    if i % 2 == 0:
        grid[q_info[i] - 1][q_info[i + 1] - 1] = 'Q'

for i in range(len(k_info)):
    if i % 2 == 0:
        grid[k_info[i] - 1][k_info[i + 1] - 1] = 'K'
for i in range(len(p_info)):
    if i % 2 == 0:
        grid[p_info[i] - 1][p_info[i + 1] - 1] = 'P'

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'Q':
            chk[i][j] += 1
            for d in range(8):
                for ln in range(1, mxln):
                    ni, nj = i + (ln * qdy[d]), j + (ln * qdx[d])
                    if not (0 <= ni < n and 0 <= nj < m) or grid[ni][nj] != '':
                        break
                    chk[ni][nj] += 1

        if grid[i][j] == 'K':
            chk[i][j] += 1
            for d in range(8):
                ni, nj = i + kdy[d], j + kdx[d]
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '':
                    chk[ni][nj] += 1

        if grid[i][j] == 'P':
            chk[i][j] += 1

answer = 0

for i in range(n):
    for j in range(m):
        if chk[i][j] == 0:
            answer += 1

print(answer)