import sys

N, M = sys.stdin.readline().split()
N = int(N)
M = int(M)
Card = sys.stdin.readline().split()
Card = list(map(int, Card))
result = 0

for i in range(0,N):
    for j in range(1,N):
        for k in range(2,N):
            if i != j and i != k and j != k:
                temp = Card[i] + Card[j] + Card[k]
            
                if result < temp <= M:
                     result = temp

print(result)
