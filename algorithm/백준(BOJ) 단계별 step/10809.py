import sys     #97 ~ 122

S = sys.stdin.readline()


for i in range(97,123):

    if chr(i) in S:
        print(S.index(chr(i)),end = " ")

    else:
        print(-1,end = " ")
