n = int(input())

k = input().split()
k = [int(j) for j in k]
sheets = 0

while k[0]%2==0 or k[1]==0:
    if k[0]%2 == 0:
        k[0] = k[0]/2
        sheets+=2
    if k[1] % 2 == 0:
        k[1] = k[1] / 2
        sheets+=2

if sheets<k[2]:
    print("NO")
else:
    print("YES")
