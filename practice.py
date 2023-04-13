n = int(input())

for i in range(n):
    j = [int(i) for i in input().split()]

    if j[0]+j[1]==j[2]:
        print("+")
    else:
        print("-")