import sys

T = int(sys.stdin.readline())

count = 0
new_count = 1

for i in range(T):

    OX = sys.stdin.readline()

    new_OX = list(map(str,list(str(OX))))  
    
    for ox in new_OX:
        if ox =='O':
            count += new_count
            new_count +=1
           
        else:
            new_count = 1
          
    print(count)
    count =0
