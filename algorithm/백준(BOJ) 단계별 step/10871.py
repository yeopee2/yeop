import sys

number = sys.stdin.readline().split(" ")

N = int(number[0])
X = int(number[1])

A = list(map(int,sys.stdin.readline().split(" ")))
    
for i in A:

    if i < X:

        print(i,end = " ")
