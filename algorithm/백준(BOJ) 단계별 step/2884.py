time = input().split(" ")

H = int(time[0])
M = int(time[1])


alarm = (H*60 + M) -45

H = alarm//60
M = alarm%60

if H == -1:
    H = 23

print(H,M)
