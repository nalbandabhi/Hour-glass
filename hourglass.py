row=int(input())
l=[]
l1=[]
for i in range(row):
    k=list(map(int,input().split()))
    l.append(k)
for i in range(row-2):
    for j in range(row-2):
        a=l[i][j]+l[i][j+1]+l[i][j+2]+l[i+1][j+1]+l[i+2][j]+l[i+2][j+1]+l[i+2][j+2]
        l1.append(a)
print(l1)
print(max(l1))        