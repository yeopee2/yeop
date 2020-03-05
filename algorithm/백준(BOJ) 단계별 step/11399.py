import sys

N = eval(sys.stdin.readline())

P = sys.stdin.readline().rstrip().split()
count = 0; total = 0

for i in range(N):
    P[i] = eval(P[i])    
P.sort()

for i in range(N):
    count += P[i]
    total += count

print(total)
