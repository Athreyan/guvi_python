le,lim=map(int,input().split())
lis=list(map(int,input().split()[:le]))
#print(lis[-1])
#print(lis[:-1])
for i in range(0,lim):
    lis=[lis[-1]]+lis[:-1]
print(*lis,end=" ")
