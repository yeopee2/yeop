import sys


music = [1,2,3,4,5,6,7,8]

reverse = [8,7,6,5,4,3,2,1]
N = list(map(int,sys.stdin.readline().split()))

if music == N:

    print("ascending")

elif reverse == N:

    print("descending")

else:

    print("mixed")
