import sys

N = int(sys.stdin.readline())


number = int(sys.stdin.readline())

numbers = list(map(int,list(str(number))))

print(sum(numbers))
