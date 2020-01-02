import sys

T = int(sys.stdin.readline())


for i in range(T):
    
    for j in range(T-i,1,-1):

        print(" ",end="")

        
    for x in range(i+1):

        print("*",end="")

    print("")
    
