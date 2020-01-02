import sys

def han_num(N):

    han = 0
    
    for n in range(N+1):
        if 1 < n < 100:
            han += 1

        elif 100 <= n < 1000:
            if ((n//100) - ((n//10)%10)) == (((n//10)%10) - (n%10)):
                han += 1
        elif n == 0:
            han += 1
        
        
    return han

def main():

    N = int(sys.stdin.readline())

    print(han_num(N))


main()
