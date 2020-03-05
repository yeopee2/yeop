import sys

P = sys.stdin.readline().rstrip().split('-')
res = 0

for i in P[0].split('+'):
    res += int(i)
for i in P[1:]:
    for j in i.split('+'):
        res -= int(j)
        
print(res)
