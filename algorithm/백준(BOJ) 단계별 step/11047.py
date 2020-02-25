import sys

N, K =  map(int, sys.stdin.readline().rstrip().split())
#기본적인 입력 받기
A = []; count = 0

for i in range(N):
    a = eval(sys.stdin.readline().rstrip())
    A.append(a)

while K != 0:
    M = max(A)
    if M > K:
        A.remove(M)
        continue
    count = count + K // max(A)
    K = K % max(A)
print(count)
