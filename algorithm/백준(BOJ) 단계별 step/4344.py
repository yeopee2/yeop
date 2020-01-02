import sys

C = int(sys.stdin.readline())

high = []
for i in range(C):

    score = list(map(int,sys.stdin.readline().split()))

    avvr = (sum(score)-score[0]) / score[0]

    stu = score[0]
    del score[0]
    for num in score:
        if num > avvr:
            high.append(num)
            
    print("%.3f" % round(len(high)/stu * 100,3)+"%")

    high = []
