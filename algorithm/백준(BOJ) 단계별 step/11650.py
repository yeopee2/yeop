import sys

N = int(sys.stdin.readline())

dot = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    dot.append((x,y))

dot.sort()
for i in dot:
    print(i[0], i[1])
