import sys

N = int(sys.stdin.readline())
result = []
for i in range(N,0,-1):
    num = N - i
    l = list(map(int,list(str(i))))
    
    if num == sum(l):
        result.append(i)
        
if len(result) == 0:
    print(0)

else:
    print(min(result))
        
