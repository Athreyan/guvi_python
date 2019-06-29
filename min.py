
num=int(input())
dd=list(map(int,input().split()[:num]))
minval=dd[0]
for i in dd:
    if(minval>i):
        minval=i
print(minval)
    
    
#sor=sorted(dd,reverse=True)
#print(sor[num-1])
