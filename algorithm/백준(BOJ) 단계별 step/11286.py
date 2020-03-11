import sys
import heapq as h

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        if x < 0:
            h.heappush(heap, (-x, x))
        else:
            h.heappush(heap, (x, x))

    elif x == 0:
        if len(heap) == 0:
            print(0)
        
        else:
            print(heap[0][1])
            h.heappop(heap)
