lenn,lim=map(int,input().split())
listt=list(map(int,input().split()[:lenn]))

for i in range(0,lim):
    listt=[listt[-1]]+listt[:-1]
print(*listt,end=" ")
