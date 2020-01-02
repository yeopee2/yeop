number = input().split(" ")

A = int(number[0])
B = int(number[1])
C = int(number[2])

if A>=B and A<=C or A<=B and A>=C:

    print(A)

elif B>=A and B<=C or B<=A and B>=C:

    print(B)

elif C>=A and C<=B or C<=A and C>=B:

    print(C)
