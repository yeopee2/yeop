import sys

N = []

for i in range(3):
    N.append(sys.stdin.readline())


num_cnt =0
A = int(N[0])
B = int(N[1])
C = int(N[2])

result = A * B * C

total =list(map(int,list(str(result))))


for i in range(10):
    print(total.count(i))

#for num in result:
