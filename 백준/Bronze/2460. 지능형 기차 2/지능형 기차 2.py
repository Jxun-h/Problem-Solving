from sys import stdin

people = 0
result = 0

for step in range(10):
    m, p = map(int, stdin.readline().rstrip().split())

    if 0 < step < 9:
        people -= m
        people += p

    else:
        people += p

    if result < people:
        result = people

print(result)