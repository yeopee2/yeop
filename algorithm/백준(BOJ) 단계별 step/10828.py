import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    command = list(sys.stdin.readline().rstrip().split())
    if len(command) > 1:
        command[1] = int(command[1])

    if command[0] == "push":
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif command[0] == "size":
        print(len(stack))

    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
