num=int(input())
ll=list(map(int,input().split()[:num]))
a=len(ll)
l2=[]
j=0
while j<a:
    if j==ll[i]:
        l2.append(j)
    j=j+1
if l2:
    print(*l2)
else:
    print("-1")
