import sys

T = int(sys.stdin.readline())

for i in range(T):

    A, B = sys.stdin.readline().split(" ")

    print("Case #%s: %s + %s = %s"%(i+1,int(A),int(B),int(A) + int(B)))
