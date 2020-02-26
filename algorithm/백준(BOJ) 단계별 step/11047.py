import sys

N, K =  map(int, sys.stdin.readline().rstrip().split())
#기본적인 입력 받기
A = []; count = 0
#필요한 리스트 및 변수 선언
for i in range(N):
    a = eval(sys.stdin.readline().rstrip())
    A.append(a)

while K != 0:
    M = max(A)
    #리스트에서 가장 큰 값을 사용해서 우선 계산하기 위해 변수 생성
    if M > K:
        A.remove(M)
        continue
    count = count + K // M
    K = K % M
print(count)
