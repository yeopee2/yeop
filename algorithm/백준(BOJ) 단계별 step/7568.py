import sys

N = int(sys.stdin.readline())
people = []
result = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))

    people.append(x)

for p in people:
    rank = 1

    for c in people:
        if p[0] != c[0] and p[1] != c[1]:
            if p[0] < c[0] and p[1] < c[1]:
                rank += 1
    result.append(rank)

for n in result:
    print(n, end =" ")
