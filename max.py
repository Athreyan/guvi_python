
num=int(input())
dd=list(map(int,input().split()[:num]))
maxval=dd[0]
for i in dd:
    if(maxval<i):
        maxval=i
print(maxval)
    
    
#sor=sorted(dd,reverse=False)
#print(sor[num-1])
