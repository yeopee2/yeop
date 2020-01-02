import sys

subject = int(sys.stdin.readline())

score = list(map(int,sys.stdin.readline().split()))

max_ = max(score)

new = []

for num in score:

    new.append(num/max_*100)
    
print("%.2f" % (sum(new)/subject))
