import sys

numbers = [int(sys.stdin.readline()) for i in range(10)]

rem_list = []  
#a =( a[i]%42 for i in range(10))    
    
for number in numbers:

    rem = number % 42
    
    if rem in rem_list:
        pass
    else:
        rem_list.append(rem)

print(len(rem_list))
