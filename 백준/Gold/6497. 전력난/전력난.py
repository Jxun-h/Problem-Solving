from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, m):
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    arr = []

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        arr.append((c, a, b))

    arr.sort()
    total, res = 0, 0

    for b in arr:
        cost, x, y = b
        total += cost

        if find_parent(parent, x) != find_parent(parent, y):
            res += cost
            union_parent(parent, x, y)

    return total - res


while 1:
    N, M = map(int, stdin.readline().split())

    if N == 0 and M == 0:
        break

    print(solution(N, M))