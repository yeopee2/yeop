import sys

N = int(sys.stdin.readline())

start = 1
plus = 6
room = 1

if N == 1:
    print(1)

else:
    while True:
        start = start + plus
        room+= 1

        if N <= start:
            print(room)
            break

        plus += 6
