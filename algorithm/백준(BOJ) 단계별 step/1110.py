import sys


N = int(sys.stdin.readline())

cycle =0

old = N

while 1:

    left = old//10
    right = old%10

    m = left + right

    if m >= 10:

        m %= 10 
        new = (right*10)+m
        
        cycle += 1

    else:
        
        new = (right*10)+m
        
        cycle += 1
    
    old = new

    if N == new:
        break
print(cycle)    
