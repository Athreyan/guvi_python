le,lim=map(int,input().split())
lis=list(map(int,input().split()[:le]))

for i in range(0,lim):
    lis=[lis[-1]]+lis[:-1]
print(*lis,end=" ")
