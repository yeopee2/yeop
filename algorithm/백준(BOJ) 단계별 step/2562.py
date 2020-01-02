import sys


List = []

for i in range(1,10):

    number = int(sys.stdin.readline())

    List.append(number)


print(max(List))
print(List.index(max(List))+1)
