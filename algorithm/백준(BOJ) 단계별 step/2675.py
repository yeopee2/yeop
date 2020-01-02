import sys

T = int(sys.stdin.readline())

for i in range(T):
    input_ = sys.stdin.readline().split()

    R = int(input_[0])

    S = list(map(str,list(str(input_[1]))))
    
    for i in range(len(S)):
        
        S[i] *= R

        if i != 0:
            S[0] += S[i]
            
            
    print(S[0])
    S = []
