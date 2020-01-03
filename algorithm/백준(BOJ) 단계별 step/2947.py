import sys

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

b = sys.stdin.readline().strip()

for i in a:
    b = b.replace(i, 'a')
    
print(len(b))
