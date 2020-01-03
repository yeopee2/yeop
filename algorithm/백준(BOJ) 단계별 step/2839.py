import sys

N = int(sys.stdin.readline())

#x,y = map(int,sys.stdin.readline().split())
  # 1
box_num = 0

while N > 0:
    if N % 5 != 0:
        N -= 3

        if N < 0:
            box_num = -1
            break

        box_num += 1

    elif N % 5 == 0:
        box_num += 1
        N -= 5

    elif N % 5 != 0 and N % 3 != 0:
        box_num = -1

print(box_num)
